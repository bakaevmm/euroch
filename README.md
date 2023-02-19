
# Technical task for research engineer position

1. [Find the python code](app/provider/provider.py) that can be used to generate prices for a preset list of financial instruments. We are expecting a CICD pipeline for packaging the container, validation, and it’s deployment. 

2. Write a client code that will be connecting to the service described in point 1, and collect generated data, for storage. Feel free to use any storage medium. Once again we are expecting a CICD pipeline for managing software delivery lifecycle.

3. Expose an endpoint for the service monitoring. Specify a set of metrics to ensure stable work of the solution.

4. Update repo with approprite documentation.

---
### ___***Request a demo from me***___

---

## Philosophy
  
   <details>
    <summary>Spoiler</summary>
      Pareto principle is used in this repository.<br>
      I see improvements, but my task was to make it simple.
   </details>
  
## Requirements
| app        | my version |
|:----------:|:----------:|
| python     |     2.7.16 |
| git        |     2.31.1 |
| vagrant    |     2.2.14 |
| virtualbox |     6.1.32 |
| ansible    |      2.8.5 |

## Summary
This repo contains the application lifecycle generating (provider) and saving (client) prices for a preset list of financial instruments.

* [Infrastructure](infra/Vagrantfile):
  * 4 VM, OS Centos 7
  * VM management - vagrant
  * VM provisioning - ansible
* [CI/CD system](infra/playbooks):
  * Self hosted gitlab server
  * Self hosted gitlab runner
* [Static analyses](cicd/test/requirements.txt):
  * Pylint
* [Deploy](cicd/roles/deploy-app):
  * Ansible
* [Monitoring](cicd/roles/deploy-monitoring):
  * Metrics for prometheus
    * Node exporter
    * Cadvisor exporter
* [Testing](cicd/test/test.sh):
  * Basic bash script


## Setup
1. Pull this repository to the workstation. 
2. Change the directory to `infra`
3. Run `vagrant up gitlab-server` command. Wait for the VM to start and set up.
4. Wait a few minutes for the gitlab server to start up.
5. Open [gitlab server](http://127.0.0.1:8080/) in your browser and log in.
   <details>
    <summary>Credentials</summary>
   login - root<br>
   password - exnesstest
   </details>
6. Import this project into gitlab - `create new project -> import project`.
7. Go to `settings -> ci/cd`, find the runner registration token and copy it.
8. On your workstation, change the directory to `/infra/playbooks`. In the `gitlab-runner.yaml` file, change the runner_token variable using the value from step 7.
9. Change the directory to `infra`.
10. Run `vagrant up` command. Wait for the VM to start and set up.
11. Using the gitlab web ui, create an empty commit. 
12. To work with the pipeline, go to `ci/cd -> pipelines`.

## Pipeline stages
1.  Static code analysis - pylint basic test.
2.  Build docker image and push to dockerhub.
3.  Deploy app to test environment.
4.  App testing - bash basic test.
5.  Deploy app to prod environment(manual step).
6.  App testing in prod environment.
7.  Deploy monitoring to prod environment(manual step).

## Extra information

* Access virtual machines via ssh
   ```
   cd infra 
   vagrant ssh {{ vm-name }}
   ```
* Access monitoring metrics
  * [server node exporter](http://localhost:9110/metrics)
  * [server cadvisor](http://localhost:9111/metrics)
  * [client node exporter](http://localhost:9120/metrics)
  * [client cadvisor](http://localhost:9121/metrics)

