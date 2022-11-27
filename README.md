<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<br />
<div align="center">
[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]

  <h3 align="center">Software Development Process</h3>

  <p align="center">
DevOps methods
(Continuous Integration, Continuous Delivery, ...) with tool support in the
application lifecycle of IoT solutions
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

DevOps platform to plan and implement a concrete IoT application example. This project consists of a Flask application running on a Raspberry Pi Zero which provides the following endpoints

* /cpu/temp: Current CPU temperature in Celsius
* /cpu/temp/error: Return "too hot" if the temperature is over 60-degree Celsius, else return "fine".
* /disk/usage: Current disk usage in percent


### Built With

* Github Actions
* Docker
* Flask

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Requirements for the project.

* Define a team-oriented, integrated process improvement approach to software
development and operations (DevOps) and implement DevOps methods
(Continuous Integration, Continuous Delivery, ...) with tool support in the
application lifecycle of IoT solutions.
* Build and commission a DevOps platform and plan and implement a concrete
IoT application example on it

### GitHub Requirements

* Public repository
* Use a project Kanban board to track your user stories
	* Steps: Todo, In Progress, Done
* Use gitflow
	* https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
* Protect your master and develop branch
	* https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/managing-a-branch-protection-rule
* Use GitHub Actions
	* feature branch
		* Build docker test stage
    * develop
        * Build docker test stage
        * Build and push dev image to DockerHub (only on push)
    * main/master
        * Build docker test stage
        * Build and push prod image to DockerHub (only on push)

        
### Application Requirements

* Flask application
* Clean application layout
       * https://flask.palletsprojects.com/en/2.2.x/tutorial/layout/
       *  https://flask.palletsprojects.com/en/2.2.x/tutorial/factory/
       *  https://flask.palletsprojects.com/en/2.2.x/tutorial/views/
* Separate requirements for each environment (test, dev and prod)
       * https://riptutorial.com/django/example/8561/using-multiple-requirements-files
* Sensor endpoints
       * /cpu/temp: Current CPU temperature in Celsius
       * /cpu/temp/error: Return "too hot" if the temperature is over 60 degree Celsius, else return "fine"
       * /disk/usage: Current disk usage in percent
* Write unit and integration tests
       * https://docs.pytest.org/en/latest/
       * https://flask.palletsprojects.com/en/2.2.x/testing/
       * Unit tests are marked as such
       * Integration test are marked as such
           * https://docs.pytest.org/en/7.1.x/example/markers.html
           * https://docs.pytest.org/en/7.1.x/how-to/mark.html
       * Mock external libraries for testing
           * https://changhsinlee.com/pytest-mock/
           * https://nedbatchelder.com/blog/201908/why_your_mock_doesnt_work.html
        * At least 80% coverage
            https://coverage.readthedocs.io/en/6.4.2/
            
            
### Docker Requirements

* Use arm32v6/python:3.9-alpine as image
* 4 Dockerfile targets
	* base
		* includes everything that all targets need
	* test
       * run linter (https://flake8.pycqa.org/en/latest/)
       * run tests (first unit tests, then integration tests)
         * coverage run -m pytest [...]
       * check coverage
         * coverage report [...]
       * fails if test coverage is below 80%
   * development
       * will start Flask server in debug mode
         * flask --debug run --host=0.0.0.0
   * production
       * will start Flask server without debug mode


<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [An awesome README template to jumpstart your projects! ](https://github.com/othneildrew/Best-README-Template)
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/DanBeluchi/sdp_project?color=green&style=for-the-badge
[contributors-url]: https://github.com/DanBeluchi/sdp_project/graphs/contributors
[issues-shield]: https://img.shields.io/github/issues/DanBeluchi/sdp_project.svg?style=for-the-badge
[issues-url]: https://github.com/DanBeluchi/sdp_project/issues
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
