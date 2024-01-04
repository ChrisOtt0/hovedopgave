package _Self.buildTypes

import jetbrains.buildServer.configs.kotlin.v2018_2.*

object BuildHovedopgave : BuildType({
    name = "Build - Hovedopgave"

    vcs {
        root(HttpsBitbucketDurrComScmPpm3phPowerModuleGitRefsHeadsSctTeamcity)
    }

    steps {
        exec {
            name = "Make - Clean"
            workingDir = "App"
            path = "make"
            arguments = "clean"
            formatStderrAsError = true
        }
        exec {
            name = "Make - Build"
            workingDir = "App"
            path = "make"
            arguments = "all -j 12"
        }
        exec {
            name = "rflash - Remote Flash"
            path = "py"
            arguments = """Tests\rflash\src\main.py -c Tests\rflash\tests\conf.toml  -b Build\PowerModule3PH_v0.0.0.hex -k D:\py-utils\agkg\tests -r 100"""
        }
        exec {
            name = "Gtest - Unittest"
            executionMode = BuildStep.ExecutionMode.RUN_ON_FAILURE
            workingDir = "Tests/gtest"
            path = "make"
            arguments = "clean runall"
        }
        exec {
            name = "Pytest - Integration"
            path = "py"
            arguments = "-m pytest Tests/pytest/test_integration.py"
        }
        exec {
            name = "Pytest - Functional"
            path = "py"
            arguments = "-m pytest Tests/pytest/test_functional.py"
        }
    }

    triggers {
        schedule {
            schedulingPolicy = daily {
                hour = 23
                minute = 55
            }
            triggerBuild = always()
        }
    }

    features {
        perfmon {
        }
    }

    requirements {
        contains("teamcity.agent.name", "Win")
    }
})
