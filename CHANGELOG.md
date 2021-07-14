# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Add group authorization to GET /events/{event_id}/images endpoint.[#716](https://github.com/rokwire/rokwire-building-blocks-api/issues/716)
- Add group authorization to GET/events/{event_id}/images/{image_id} endpoint.[#718](https://github.com/rokwire/rokwire-building-blocks-api/issues/718)
- Add group authorization to PUT/events/{event_id}/images/{image_id} endpoint.[#719](https://github.com/rokwire/rokwire-building-blocks-api/issues/719)
- Add group authorization to DELETE /events/{event_id}/images/{image_id} endpoint.[#720](https://github.com/rokwire/rokwire-building-blocks-api/issues/720)

## [1.10.0] - 2021-06-29
### Added
- Add endpoints for listing contributions, capabilities, and talents. [#602](https://github.com/rokwire/rokwire-building-blocks-api/issues/602)
- Add query parameters to contribution building block's api spec and function arguments. [#616](https://github.com/rokwire/rokwire-building-blocks-api/issues/616)
- Add user auth to Events Building Block yml file. [#598](https://github.com/rokwire/rokwire-building-blocks-api/issues/598)
- Use dovenv library for organizing enviroment variables.[#614](https://github.com/rokwire/rokwire-building-blocks-api/issues/614)
- Add CORS support for Contribution Building Block.[#621](https://github.com/rokwire/rokwire-building-blocks-api/issues/621)
- Add login option for Contribution Catalog.[#634](https://github.com/rokwire/rokwire-building-blocks-api/issues/634)
- Add logout option for Contribution Catalog.[#636](https://github.com/rokwire/rokwire-building-blocks-api/issues/636)
- Update event schema to add new field createdByGroupId.[#396](https://github.com/rokwire/rokwire-building-blocks-api/issues/396)
- Add ApiKeyAuth and status to contribution building block.[#654](https://github.com/rokwire/rokwire-building-blocks-api/issues/654)
- Add ids to capability and talent.[#661](https://github.com/rokwire/rokwire-building-blocks-api/issues/661)
- Add auth check for login required pages.[#657](https://github.com/rokwire/rokwire-building-blocks-api/issues/657)
- Add /contribute as prefix for ./profile page. [#663](https://github.com/rokwire/rokwire-building-blocks-api/issues/663)
- Add UUID for capability and talent in Contribution Catalog.[#666](https://github.com/rokwire/rokwire-building-blocks-api/issues/666)
- Add autocomplete feature when inputting admin name for contribution catalog.[#665](https://github.com/rokwire/rokwire-building-blocks-api/issues/665)
- Add search endpoints using capability and talent id.[#662](https://github.com/rokwire/rokwire-building-blocks-api/issues/662)
- Add release script for Contributions Building Block.[#675](https://github.com/rokwire/rokwire-building-blocks-api/issues/675)
- Add okay endpoint to Contributions Building Block.[#679](https://github.com/rokwire/rokwire-building-blocks-api/issues/679)
- Add isGroupPrivate to Events schema.[#682](https://github.com/rokwire/rokwire-building-blocks-api/issues/682)
- Add group authorization to GET /events endpoint. [#683](https://github.com/rokwire/rokwire-building-blocks-api/issues/683), [#684](https://github.com/rokwire/rokwire-building-blocks-api/issues/684)
- Add reviewers management endpoints. [#692](https://github.com/rokwire/rokwire-building-blocks-api/issues/692)
- Add get group event by groupid parameter.[#685](https://github.com/rokwire/rokwire-building-blocks-api/issues/685)
- Add isEventFree field to Events Building Block yaml file.[#695](https://github.com/rokwire/rokwire-building-blocks-api/issues/695)
- Add group authroziation on get event endpoint.[#693](https://github.com/rokwire/rokwire-building-blocks-api/issues/693)
- Add basic detailed views for Contributions, Talents, and Capabilities. [#638](https://github.com/rokwire/rokwire-building-blocks-api/issues/638), [#669](https://github.com/rokwire/rokwire-building-blocks-api/issues/669), [#670](https://github.com/rokwire/rokwire-building-blocks-api/issues/670)
- Add group authroziation on put event endpoint.[#699](https://github.com/rokwire/rokwire-building-blocks-api/issues/699)
- Add group authroziation on patch event endpoint.[#701](https://github.com/rokwire/rokwire-building-blocks-api/issues/701)
- Add group authroziation on deletion event endpoint[#700](https://github.com/rokwire/rokwire-building-blocks-api/issues/700)

### Fixed
- Fix Contribution catalog's home page display issue. [#448](https://github.com/rokwire/rokwire-building-blocks-api/pull/448)
- Use dovenv library for organizing enviroment variables. [#614](https://github.com/rokwire/rokwire-building-blocks-api/issues/614)
- Add CORS support for Contribution Building Block. [#617](https://github.com/rokwire/rokwire-building-blocks-api/issues/617)
- Add strict validation in Contribution Building Block. [#627](https://github.com/rokwire/rokwire-building-blocks-api/issues/627)
- Add authentication and authorization using GitHub account in Contribution Building Block. [#635](https://github.com/rokwire/rokwire-building-blocks-api/issues/635)
- Add github authorization in new contribution post via catalog. [#647](https://github.com/rokwire/rokwire-building-blocks-api/issues/647)
- Fix date format issue in the events endpoint of GET /events/<id>. [#438](https://github.com/rokwire/rokwire-building-blocks-api/issues/438)
- Fix error code in GET /contributions/{contributionID}. [#672](https://github.com/rokwire/rokwire-building-blocks-api/issues/672)
- Fix status in contribution. [#668](https://github.com/rokwire/rokwire-building-blocks-api/issues/668)
- Fix returning an object when there is only single result in GET /contributions. [#681](https://github.com/rokwire/rokwire-building-blocks-api/issues/681)

### Changed
- Updated CODEOWNERS file. [#631](https://github.com/rokwire/rokwire-building-blocks-api/issues/631)
- Modified environmental variables in Dockerfile. [#677](https://github.com/rokwire/rokwire-building-blocks-api/issues/677)
- Updated pre-commit config and corresponding GitHub Action to use `Yelp/detect-secrets` version 1.0.3. [#649](https://github.com/rokwire/rokwire-building-blocks-api/issues/649) 
- Updated location description in Events Building Block. [#706](https://github.com/rokwire/rokwire-building-blocks-api/issues/706)

### Removed
- Remove db index on sponsor field. [#686](https://github.com/rokwire/rokwire-building-blocks-api/issues/686)

## [1.9.1] - 2021-02-22
### Fixed
- Fix Docker build errors. [#633](https://github.com/rokwire/rokwire-building-blocks-api/issues/633)

## [1.9.0] - 2020-12-17
### Fixed
- Fix the error code to 400 on events missing fields query. [#448](https://github.com/rokwire/rokwire-building-blocks-api/pull/448)
- Text changes to Contributions Catalog. [#601](https://github.com/rokwire/rokwire-building-blocks-api/issues/601)

### Added
- Add capabilities dataset in contribution building block. [#401](https://github.com/rokwire/rokwire-building-blocks-api/issues/401)
- Add contribution building block. [#406](https://github.com/rokwire/rokwire-building-blocks-api/issues/406)
- Add talent data to contribution dataset. [#407](https://github.com/rokwire/rokwire-building-blocks-api/issues/407)
- Add search option in contribution and capability dataset. [#458](https://github.com/rokwire/rokwire-building-blocks-api/issues/458)
- Contributor guidelines. [#572](https://github.com/rokwire/rokwire-building-blocks-api/issues/572)
- A pull request template. [#573](https://github.com/rokwire/rokwire-building-blocks-api/issues/573)
- Add Contributions Catalog Frontend. [#462](https://github.com/rokwire/rokwire-building-blocks-api/issues/462)
- Add Github authentication for Contributions Catalog. [#580](https://github.com/rokwire/rokwire-building-blocks-api/issues/580)
- Add Rokwire Group admins AD group to list of authorized event write groups. [#607](https://github.com/rokwire/rokwire-building-blocks-api/issues/607)

## Changed
- Separated contribution yaml from rokwire.yaml. [#514](https://github.com/rokwire/rokwire-building-blocks-api/issues/514)
- Timestamp format for non pii dataset has been changed. [#566](https://github.com/rokwire/rokwire-building-blocks-api/issues/566)
- Apply query parameters to subevent search. [#581](https://github.com/rokwire/rokwire-building-blocks-api/issues/581)
- Support multiple groups when doing authorization. [#447](https://github.com/rokwire/rokwire-building-blocks-api/issues/447)
- Support events building block group authorization. [#596](https://github.com/rokwire/rokwire-building-blocks-api/issues/596)

## [1.8.0] - 2020-10-01
### Added
- Add multiple client id ability to auth library. [#548](https://github.com/rokwire/rokwire-building-blocks-api/issues/548)
- Add more time range query parameters to events yml and Readme.[#551](https://github.com/rokwire/rokwire-building-blocks-api/issues/551)
- Add query parameters to enhance events search. [#551](https://github.com/rokwire/rokwire-building-blocks-api/issues/551)

### Fixed
- Replace the record on put endpoint. [#550](https://github.com/rokwire/rokwire-building-blocks-api/issues/550)
- Runtime error in building blocks by updating gunicorn and gevent versions. [#560](https://github.com/rokwire/rokwire-building-blocks-api/issues/560)
- Runtime error when Auth Library validates manually generated ID tokens. [#562](https://github.com/rokwire/rokwire-building-blocks-api/issues/562)

### Changed
- Disabled logger to provide detailed PII information in profile BB. [#556](https://github.com/rokwire/rokwire-building-blocks-api/issues/556)
- Update base docker image when doing release. [#564](https://github.com/rokwire/rokwire-building-blocks-api/issues/564)

## [1.7.0] - 2020-09-03
### Added
- Add Standard License Header for Events Building Block. [#480](https://github.com/rokwire/rokwire-building-blocks-api/issues/480)
- Add Standard License Header for Authentication Building Block. [#497](https://github.com/rokwire/rokwire-building-blocks-api/issues/497)
- Add Standard License Header for Authentication Library. [#498](https://github.com/rokwire/rokwire-building-blocks-api/issues/498)
- Add CODEOWNERS file. [#508](https://github.com/rokwire/rokwire-building-blocks-api/issues/508)
- Add Standard License Header for API Doc. [#501](https://github.com/rokwire/rokwire-building-blocks-api/issues/501)
- Add bug report and feature request issue templates. [#510](https://github.com/rokwire/rokwire-building-blocks-api/issues/510)
- Add Talent Chooser Building Block APIs documentation. [#528](https://github.com/rokwire/rokwire-building-blocks-api/issues/528)
- Add flags isVirtual and displayOnlyWithSuperEvent to events schema. [#542](https://github.com/rokwire/rokwire-building-blocks-api/issues/542), [#541](https://github.com/rokwire/rokwire-building-blocks-api/issues/541)
- Add `startDateLimit` query parameter to events search endpoint. [#545](https://github.com/rokwire/rokwire-building-blocks-api/issues/545)

### Changed
- OpenAPI specification file rokwire.yaml file split across different building blocks. [#485](https://github.com/rokwire/rokwire-building-blocks-api/issues/485)
- Update Swagger-UI version. [#500](https://github.com/rokwire/rokwire-building-blocks-api/issues/500)
- Rokwire API Doc Dockerfile to integrate multiple OpenAPI specifications file. [#486](https://github.com/rokwire/rokwire-building-blocks-api/issues/486)
- Update Appconfig Building Block docker base image. [#515](https://github.com/rokwire/rokwire-building-blocks-api/issues/515)
- Update Authentication Building Block docker base image. [#517](https://github.com/rokwire/rokwire-building-blocks-api/issues/517)
- Update Authentication Building Block README. [#519](https://github.com/rokwire/rokwire-building-blocks-api/issues/519)
- Changed docker base image for Profile and Logging Building Block. [#521](https://github.com/rokwire/rokwire-building-blocks-api/issues/521)
- Changed README for auth-middleware-test-svc based on new change. [#523](https://github.com/rokwire/rokwire-building-blocks-api/issues/523)
- Update issue template. [#537](https://github.com/rokwire/rokwire-building-blocks-api/issues/537)
- Update README. [#539](https://github.com/rokwire/rokwire-building-blocks-api/issues/539)

### Removed
- rokwire.yaml file and deployment scripts that were not getting used. [#486](https://github.com/rokwire/rokwire-building-blocks-api/issues/486)

### Fixed
- Docker image vulnerabilities in Authentication Building Block. [#499](https://github.com/rokwire/rokwire-building-blocks-api/issues/499)
- Docker image vulnerabilities in Events Building Block. [#484](https://github.com/rokwire/rokwire-building-blocks-api/issues/484)
- Re-fixed bug related to including .env files in docker images. [#419](https://github.com/rokwire/rokwire-building-blocks-api/issues/419)

### Security
- Add Yelp's Secret Detector. [#530](https://github.com/rokwire/rokwire-building-blocks-api/issues/530)
- Update secret baseline file. [#532](https://github.com/rokwire/rokwire-building-blocks-api/issues/532)

## [1.6.0] - 2020-07-14
- Add Health Building Block APIs documentation. [#468](https://github.com/rokwire/rokwire-building-blocks-api/issues/468)
- Code of Conduct. [#487](https://github.com/rokwire/rokwire-building-blocks-api/issues/487)

### Changed
- App Config database and collection names are now configurable via environment variables. [#492](https://github.com/rokwire/rokwire-building-blocks-api/issues/492)

### Fixed
- Docker image vulnerabilities in App Config Building Block. [#482](https://github.com/rokwire/rokwire-building-blocks-api/issues/482)

## [1.5.0] - 2020-07-01
### Added
- Add environment variable for on/off of printing logs out. [#459](https://github.com/rokwire/rokwire-building-blocks-api/issues/459)
- LICENSE file. [#466](https://github.com/rokwire/rokwire-building-blocks-api/issues/466)
- Add documentType field in PII dataset. [#473](https://github.com/rokwire/rokwire-building-blocks-api/issues/473)
- Add standard license header to code file [#470](https://github.com/rokwire/rokwire-building-blocks-api/issues/470)
- Add license header for app config building block [#470](https://github.com/rokwire/rokwire-building-blocks-api/issues/470)
- Add enum value to documentType field in PII. [#476](https://github.com/rokwire/rokwire-building-blocks-api/issues/476)

## [1.4.0] - 2020-06-11
### Added
- Index to PII and Non-PII database collections. [#428](https://github.com/rokwire/rokwire-building-blocks-api/issues/428)
- Add search option in contribution and capability dataset. [#458](https://github.com/rokwire/rokwire-building-blocks-api/issues/458)

### Changed
- Incoming requests can be validated against a list of API keys. [#277](https://github.com/rokwire/rokwire-building-blocks-api/issues/277)

## [1.3.1] - 2020-06-05
### Changed
- Stop printing logs in the Logging Building Block. [#444](https://github.com/rokwire/rokwire-building-blocks-api/issues/444)

## [1.3.0] - 2020-05-15
### Added
- Add more fields in PII and updated API design. [#411](https://github.com/rokwire/rokwire-building-blocks-api/issues/411)
- Couple of examples to Profile PII API documentation. [#426](https://github.com/rokwire/rokwire-building-blocks-api/issues/426)

### Changed
- Differentiated verified and unverified data items in PII data and made unverified data updatable. [#424](https://github.com/rokwire/rokwire-building-blocks-api/issues/424)
- Some PII data fields became read-only (pid, creation date). [#431](https://github.com/rokwire/rokwire-building-blocks-api/issues/431)

### Removed
- Read-only property from couple of PII fields. [#432](https://github.com/rokwire/rokwire-building-blocks-api/issues/432)

### Fixed
- Date string fields in PII examples. [#434](https://github.com/rokwire/rokwire-building-blocks-api/issues/434)
- Couple of CHANGELOG entries. [#436](https://github.com/rokwire/rokwire-building-blocks-api/issues/436) 

## [1.2.2] - 2020-05-03
## Fixed
- Bug related to including env file in docker image. [#419](https://github.com/rokwire/rokwire-building-blocks-api/issues/419)

## [1.2.1] - 2020-05-01
### Fixed
- Version number in API Design YAML file. [#414](https://github.com/rokwire/rokwire-building-blocks-api/issues/414)

## [1.2.0] - 2020-03-24
### Added
- Add capabilities dataset in contribution building block. [#401](https://github.com/rokwire/rokwire-building-blocks-api/issues/401)
- Add contribution building block. [#406](https://github.com/rokwire/rokwire-building-blocks-api/issues/406)
- Add environment variable to set url prefix for the connexion events building block. [#369](https://github.com/rokwire/rokwire-building-blocks-api/issues/369)
- Add super events tag to refactoring branch. [#316](https://github.com/rokwire/rokwire-building-blocks-api/issues/316)
- Get events by multiple event ids. [#268](https://github.com/rokwire/rokwire-building-blocks-api/issues/268)
- Add dnspython module to enable mongodb+srv:// URIs [#235](https://github.com/rokwire/rokwire-building-blocks-api/issues/235)
- API design changes to support super events. [#302](https://github.com/rokwire/rokwire-building-blocks-api/issues/302)
- Add an optional `upgrade` object in app config [#328](https://github.com/rokwire/rokwire-building-blocks-api/issues/328)
- Add a method to auth_middleware library for doing authorization. [#342](https://github.com/rokwire/rokwire-building-blocks-api/issues/342)
- Add a base path to logging and profiles service. [#362](https://github.com/rokwire/rokwire-building-blocks-api/issues/362)
- Add a base path to appconfig service. [#364](https://github.com/rokwire/rokwire-building-blocks-api/issues/364)
- Add error handlers in posting PII. [#376](https://github.com/rokwire/rokwire-building-blocks-api/issues/376)
- Add nullable to several non-pii fields. [#398](https://github.com/rokwire/rokwire-building-blocks-api/issues/398)
- Add endpoint for filtering non-pii data by using eventIds. [#391](https://github.com/rokwire/rokwire-building-blocks-api/issues/391)

### Changed
- Refactored Profile building block using connexion. [#284](https://github.com/rokwire/rokwire-building-blocks-api/issues/284)
- Update release script to build and push refactoring branch docker image. [#308](https://github.com/rokwire/rokwire-building-blocks-api/issues/308)
- Refactored App Config building block using connexion. [#294](https://github.com/rokwire/rokwire-building-blocks-api/issues/294)
- Refactored Events Building Block using connexion. [#296](https://github.com/rokwire/rokwire-building-blocks-api/issues/296)
- Set App Config Building Block's debug flag to false by default. [#332](https://github.com/rokwire/rokwire-building-blocks-api/issues/332)
- UUID entry for posting new PII dataset changed to list from string. [#329](https://github.com/rokwire/rokwire-building-blocks-api/issues/329)
- Update authorization calls in refactored Events, Profile, and App Config building blocks. [#342](https://github.com/rokwire/rokwire-building-blocks-api/issues/342)

### Fixed
- fix the return code when delete on a non-existing event.
- Issue with incompatible Python and Connexion version in Authentication Building Block. [#389](https://github.com/rokwire/rokwire-building-blocks-api/issues/389)
- Issue with date time format in event response. [#402](https://github.com/rokwire/rokwire-building-blocks-api/issues/402)
- Issue with fields that need to be marked as nullable. [#409](https://github.com/rokwire/rokwire-building-blocks-api/issues/409)

## [1.0.6] - 2020-02-25
### Added
- Compatibility in Profile PII's UUID for string and list [#372](https://github.com/rokwire/rokwire-building-blocks-api/issues/372)

### Fixed
- Profile PII PUT endpoint related to updating UUID list [#372](https://github.com/rokwire/rokwire-building-blocks-api/issues/372)

## [1.0.5] - 2020-02-05
### Added
- Add super event tags. 
- Add super event tags endpoint into rokwire.yaml file.

### Fixed
- Super events operation Id.

## [1.0.4] - 2020-01-17
### Added
- API design and code changes to support super events. [#302](https://github.com/rokwire/rokwire-building-blocks-api/issues/302)

## [1.0.3] - 2019-12-06
### Added
- Get events by multiple event ids.
- Add dnspython module to enable mongodb+srv:// URIs [#235](https://github.com/rokwire/rokwire-building-blocks-api/issues/235)

### Changed
- Update Events Service Readme to add CACHE_DIRECTORY. [#275](https://github.com/rokwire/rokwire-building-blocks-api/issues/275)

## [1.0.2] - 2019-10-30
### Changed
- Updated version number and server URLs in API definition. [#269](https://github.com/rokwire/rokwire-building-blocks-api/issues/269)

## [1.0.1] - 2019-10-30
### Fixed
- Updated CHANGELOGs with release information. [#256](https://github.com/rokwire/rokwire-building-blocks-api/issues/265)

## [1.0.0] - 2019-10-10
### Added
- Add Docker env for AWS fargate deploy
- Add recurring event search
- Add events multiple titles search.
- Add skip and limit on events query.
- This CHANGELOG file
- Events Building Block.
- Issue template.
- Definitions for PUT method for events in YAML file.
- Fields to event schema for storing submission status and date modified.
- Scripts for deploying Swagger docker to host Rokwire API document on AWS
- Profile Building Block
- Added time stamp
- Checking method for email and phone number to prevent duplicate entry
- Profile rest service dockerized
- Image update and fileDescriptor moved to pii from non-pii
- Test profiles building block rest service deployed in AWS server
- Add searching by mobile app version feature to App Config API
- Add secretKeys to App Config
- Logging building block API definitions.
- Auth middleware library.
- Dockerfile for Rokwire Platform API documentation and updated README.
- Add caching to app-config and events GET endpoints.
- Create profile data model boiler plate. [SCCI-103](https://opensource.ncsa.illinois.edu/jira/browse/SCCI-103)
- Created profile restservice boiler plate. [SCCI-130](https://opensource.ncsa.illinois.edu/jira/browse/SCCI-130)
- Added time stamp. [SCCI-131](https://opensource.ncsa.illinois.edu/jira/browse/SCCI-131)
- Added age over 13. [SCCI-132](https://opensource.ncsa.illinois.edu/jira/browse/SCCI-132)
- Checking method for email and phone number to prevent duplicate entry. [#37](https://github.com/rokwire/rokwire-building-blocks-api/issues/37)
- Profile rest service dockerized. [#62](https://github.com/rokwire/rokwire-building-blocks-api/issues/62)
- Added favorites. [#115](https://github.com/rokwire/rokwire-building-blocks-api/issues/115)
- Added positive and negative interest tags. [#116](https://github.com/rokwire/rokwire-building-blocks-api/issues/116)
- Added an ability to store and retrieve schema free information. [#117](https://github.com/rokwire/rokwire-building-blocks-api/issues/117)
- Added privacySettings in PII data model. [#138](https://github.com/rokwire/rokwire-building-blocks-api/issues/138)
- created initial logging building block end point. [#61](https://github.com/rokwire/rokwire-building-blocks-api/issues/61)
- created a sample logging data. [#173](https://github.com/rokwire/rokwire-building-blocks-api/issues/173)

### Changed
- download events image file from S3 without checking the image id from db.
- add events building block S3 folder as env variable.
- events tag search has been changed to logic or.
- Update events schema to remove endDate as required field and add createdBy and createDate.
- Update events schema according to discussion and feedback.
- Update rokwire.yaml for events build block.
- Update rokwire.yaml for API endpoint authentication.
- Update README to include how to view Rokwire API document using Swagger
- The code repository name to rokwire-building-blocks-api.
- Fix README to use updated API definition YAML file URL.
- Fix API definition YAML file to use rokwire instead of SCCI.
- Add App Config API definition to Swagger YAML file
- Events building block API definition and schema to include event categories and sub categories
- Separated non-pii data and pii data and database in profile building block
- Profile building block rest api changed to Flask RESTFul api service
- Profile building block non-pii interests has been changed by using category and subcategory
- Update rokwire.yaml for images entry points of events building block
- Temporarily ignoring `targetAudience` search query string in events.
- Changed api doc path from http://.../api/docs to http://.../docs since our domain api.rokwire.illinois.edu contains "api" word.
- Update Events schema to include registrationLabel
- Gunicorn gevent worker class to increase performance.
- Make better use of event category indexes for performance.
- Sort events by startDate and then endDate.
- Switch profile service to use gunicorn.
- Redirect events images to S3 instead of trying to serve them directly.
- Separated non-pii data and pii data
- Separated non-pii and pii database
- Image update and fileDescriptor moved to pii from non-pii
- Separated non-pii data and pii data. [SCCI-104](https://opensource.ncsa.illinois.edu/jira/browse/SCCI-104)
- Separated non-pii and pii database. [SCCI-123](https://opensource.ncsa.illinois.edu/jira/browse/SCCI-123)
- Image update and fileDescriptor moved to pii from non-pii. [#72](https://github.com/rokwire/rokwire-building-blocks-api/issues/72)
- Separated non-pii and pii database url. [#73](https://github.com/rokwire/rokwire-building-blocks-api/issues/73)
- Profile building block rest api changed to Flask RESTFul api service. [#31](https://github.com/rokwire/rokwire-building-blocks-api/issues/31)
- Non-pii interests has been modified with category and subcategory. [#86](https://github.com/rokwire/rokwire-building-blocks-api/issues/86)
- README file has examples for the endpoints. [#119](https://github.com/rokwire/rokwire-building-blocks-api/issues/119)
- Database indexing system changed for document DB. [#127](https://github.com/rokwire/rokwire-building-blocks-api/issues/127)
- Updated logging system based on Flask RESTFul service. [#130](https://github.com/rokwire/rokwire-building-blocks-api/issues/130)
- Made profile building block flask using the flask server configuration. [#92](https://github.com/rokwire/rokwire-building-blocks-api/issues/92)
- Modified profiles building block's rest endpoint prefix to environmental variable. [#187](https://github.com/rokwire/rokwire-building-blocks-api/issues/197)
- Modified profiles building block's log to show the endpoint information. [#244](https://github.com/rokwire/rokwire-building-blocks-api/issues/244)
- Created a method for checking the id information by comparing id token and db information. [#66](https://github.com/rokwire/rokwire-building-blocks-api/issues/66)
- Information in the id token is used for creating and updating the pii dataset. [#257](https://github.com/rokwire/rokwire-building-blocks-api/issues/257)
- URL prefix to be configurable. [#181](https://github.com/rokwire/rokwire-building-blocks-api/issues/181)
- All log entries are inserted in one database call.

### Fixed
- Events building block API definition to improve text.
- API documentation in YAML file to reflect the latest code and made text improvements.
- Issues with API specification YAML file related to app config building block.
- Indentation issues with API specification YAML file
- MongoClient use in several blocks broke connection pooling
- Don't send clickstream logs through the logging library

### Removed
- References to AWS keys and variables in the Events Building Block.

[Unreleased]: https://github.com/rokwire/rokwire-building-blocks-api/compare/1.10.0...HEAD
[1.10.0]: https://github.com/rokwire/rokwire-building-blocks-api/compare/1.9.1...1.10.0
[1.9.1]: https://github.com/rokwire/rokwire-building-blocks-api/compare/1.9.0...1.9.1
[1.9.0]: https://github.com/rokwire/rokwire-building-blocks-api/compare/1.8.0...1.9.0
[1.8.0]: https://github.com/rokwire/rokwire-building-blocks-api/compare/1.7.0...1.8.0
[1.7.0]: https://github.com/rokwire/rokwire-building-blocks-api/compare/1.6.0...1.7.0
[1.6.0]: https://github.com/rokwire/rokwire-building-blocks-api/compare/1.5.0...1.6.0
[1.5.0]: https://github.com/rokwire/rokwire-building-blocks-api/compare/1.4.0...1.5.0
[1.4.0]: https://github.com/rokwire/rokwire-building-blocks-api/compare/1.3.1...1.4.0
[1.3.1]: https://github.com/rokwire/rokwire-building-blocks-api/compare/1.3.0...1.3.1
[1.3.0]: https://github.com/rokwire/rokwire-building-blocks-api/compare/1.2.2...1.3.0
[1.2.2]: https://github.com/rokwire/rokwire-building-blocks-api/compare/1.2.1...1.2.2
[1.2.1]: https://github.com/rokwire/rokwire-building-blocks-api/compare/1.2.0...1.2.1
[1.2.0]: https://github.com/rokwire/rokwire-building-blocks-api/compare/1.0.6...1.2.0
[1.0.6]: https://github.com/rokwire/rokwire-building-blocks-api/compare/1.0.5...1.0.6
[1.0.5]: https://github.com/rokwire/rokwire-building-blocks-api/compare/1.0.4...1.0.5
[1.0.4]: https://github.com/rokwire/rokwire-building-blocks-api/compare/1.0.3...1.0.4
[1.0.3]: https://github.com/rokwire/rokwire-building-blocks-api/compare/1.0.2...1.0.3
[1.0.2]: https://github.com/rokwire/rokwire-building-blocks-api/compare/1.0.1...1.0.2
[1.0.1]: https://github.com/rokwire/rokwire-building-blocks-api/compare/1.0.0...1.0.1
[1.0.0]: https://github.com/rokwire/rokwire-building-blocks-api/releases/tag/1.0.0
