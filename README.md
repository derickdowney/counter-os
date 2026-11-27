# Quick Start

## Neovim Development Environment
To setup the Neovim dev workspace for this:
- In your terminal, navigate to this project directory
- Run `source .venv/bin/activate`
- Run `nvim -S session.vim`
- Navigate to bottom-left terminal and run `source .venv/bin/activate`

## Running Tests
In neovim:
- Press `0-` to run unit tests
- Press `0=` to run unit and integration tests

## Running Application
- Create ".env" file at project root (refer to ".env-template")
- If using "postgres_local", run this command in terminal first:
    - `docker-compose up -d`





# Clean Architecture Overview

## Domain Layer

### Entities
Fundamental objects that model the business domain.
May contain state and/or behavior.
Could throw DomainExceptions to enforce "domain invariants."

### Value Objects
Objects that represent "values" held by entities.
Immutable and contain state only.
Best place to throw DomainExceptions to enforce "domain invariants."

### Services (?)
Objects for behaviors not clearly owned by any one entity.
...may throw DomainExceptions?

### Repositories
Objects that contain collections of entities.

### Exceptions
DomainExceptions signify a "bussiness rule" ("domain invariants") was broken.




## Application Layer

### DTOs (Data Transfer Objects)

#### Requests
"Request" DTOs do the following:
- Convert "generic objects" into "domain objects"
- Can raise exceptions at two stages during operation lifecycle
- `__init__()` construction stage:
    - Happens in Interface Layer in a `Controller` object's `handle` method
    - Converts external input into "request inputs, as generic types"
    - Raises `ValueErrors` if generic types are invalid
        - (e.g., if request init requires an int but was passed a string or list)
- `to_execution_params()` execution phase:
    - Happens in Application Layer in a `UseCase` object's `execute` method
    - Converts request inputs from "generic types" to "domain types"
    - Propagates exceptions from Domain Value Objects if conversion fails
        - (e.g., request int is negative and value object can't be negative)

#### Responses
"Response" DTOs do the following:
- Convert "domain objects" into "generic objects"
- Also convert domain exceptions into "generic objects"
    - (e.g., `ErrorResponse.cant_be_negative(-1)` returns object with
             "str" error message and "str" error code)
- Never throws any exceptions itself! Used to "return errors as values"
- Constructed and returned at the very end of a `UseCase` in Application Layer


### Results
`Result` is union type capturing either `Success` or `Error` objects
`Success` object contains a `SuccessResponse` DTO
`Error` object contains a `ErrorResponse` DTO

### Use Cases
Interactions of domain entities, value objects, repositories, and services
Optionally accepts a "Request" DTO argument
Always returns a `Result` object
Catches all possible DomainExceptions and returns them as values (or objects)
- If exception, returns `Error` with `ErrorResponse` describing exception
- If no exception, returns `Success` with `SuccessResponse` specific to use case




## Interface Layer

### Presenter
`ThingPresenter` takes a Response DTO and converts it into a `ThingViewModel`
- `ThingPresenter.present_success_response()` takes SuccessReponse DTO as arg
- `ThingPresenter.present_error_response()` takes ErrorResponse DTO as arg
Each presentation framework requires its own Presenter. For example:
- `CliCounterPresenter` presents counters for CLI applicaiton
- `WebCounterPresenter` presents counters for web application

### ViewModel
`ViewModel` is a "humble object" that simply "displays pre-formatted data."
There is only one `ThingViewModel` per thing! Each presentation framework
uses the same exact `ThingViewModel`. There is no `CliThingViewModel`.

### OperationResult
`OperationResult` is union type for `OperationSuccess` or `OperationError` types
`OperationSuccess` object contains a ` SuccessViewModel`
`OperationError` object contains an `ErrorViewModel`
All `Controller.handle_xxx()` methods return an `OperationResult`

### Controller
Constructed with all possible use cases and presenters
`handle_xxx()` methods:
- take in generic input
- initialize `Request` DTO using generic input
    - if init throws `ValueError` exception
        catch exception
        create `ErrorResponse` DTO from exception
        use `Presenter` to convert `ErrorResponse` into `ErrorViewModel`
        return `OperationError` containing `ErrorViewModel`
- call `UseCase` with `Request` DTO as argument
    - if `UseCase` returns `Success` object
        use `Presenter` to convert `SuccessResponse` into `SuccessViewModel`
        return `OperationSuccess` containing `SuccessViewModel`
    - if `UseCase` returns `Error` object
        use `Presenter` to convert `ErrorResponse` into `ErrorViewModel`
        return `OperationError` containing `ErrorViewModel`


