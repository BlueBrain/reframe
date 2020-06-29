<a href="http://github.com/eth-cscs/reframe">
  <img src="docs/_static/img/reframe_logo-full.png" width=400>
</a>

[![Build Status](https://travis-ci.org/eth-cscs/reframe.svg?branch=master)](https://travis-ci.org/eth-cscs/reframe)
[![Documentation Status](https://readthedocs.org/projects/reframe-hpc/badge/?version=latest)](https://reframe-hpc.readthedocs.io/en/latest/?badge=latest)
[![codecov.io](https://codecov.io/gh/eth-cscs/reframe/branch/master/graph/badge.svg)](https://codecov.io/github/eth-cscs/reframe)<br/>
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/eth-cscs/reframe?include_prereleases)
![GitHub commits since latest release](https://img.shields.io/github/commits-since/eth-cscs/reframe/latest)
![GitHub contributors](https://img.shields.io/github/contributors-anon/eth-cscs/reframe)<br/>
[![PyPI version](https://badge.fury.io/py/ReFrame-HPC.svg)](https://badge.fury.io/py/ReFrame-HPC)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/reframe-hpc)<br/>
[![Slack](https://reframe-slack.herokuapp.com/badge.svg)](https://reframe-slack.herokuapp.com/)<br/>
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

# ReFrame in a Nutshell

ReFrame is a framework for writing regression tests for HPC systems.
The goal of this framework is to abstract away the complexity of the interactions with the system, separating the logic of a regression test from the low-level details, which pertain to the system configuration and setup.
This allows users to write easily portable regression tests, focusing only on the functionality.

Regression tests in ReFrame are simple Python classes that specify the basic parameters of the test.
The framework will load the test and will send it down a well-defined pipeline that will take care of its execution.
The stages of this pipeline take care of all the system interaction details, such as programming environment switching, compilation, job submission, job status query, sanity checking and performance assessment.

Writing system regression tests in a high-level modern programming language, like Python, poses a great advantage in organizing and maintaining the tests.
Users can create their own test hierarchies, create test factories for generating multiple tests at the same time and also customize them in a simple and expressive way.

## Getting ReFrame on BB5

Clone ReFrame fork from BlueBrain organisation on BB5:

```bash
git clone https://github.com/BlueBrain/reframe.git -b bbp
```

Initialize environment:

```bash
cd reframe
module load unstable python
python -mvenv devenv
. ./devenv/bin/activate
pip install -r requirements.txt
```

Now ReFrame should be ready to use:

```bash
./bin/reframe -h
usage: reframe [-h] [--prefix DIR] [-o DIR] [-s DIR] [--timestamp [TIMEFMT]]

optional arguments:
  -h, --help            show this help message and exit

Options controlling ReFrame output:
  --prefix DIR          Set general directory prefix to DIR
  -o DIR, --output DIR  Set output directory prefix to DIR
  -s DIR, --stage DIR   Set stage directory prefix to DIR
..
```

See BB5 config using:

```bash
./bin/reframe -C config/bb5.py --system=bb5 --show-config
```

Run basic test on BB5:

```bash
./bin/reframe -C config/bb5.py --system=bb5:login -c tutorial/example1.py -r
...
[ReFrame Setup]
  version:           3.1-dev0 (rev: b2b3b6be)
  command:           './bin/reframe -C config/bb5.py --system=bb5:login -c tutorial/example1.py -r'
  launched by:       kumbhar@bbpv1.epfl.ch
  working directory: '/gpfs/bbp.cscs.ch/data/project/proj16/kumbhar/pramod_scratch/reframe_test/reframe'
  settings file:     '/tmp/tmppl89y40h.py'
  check search path: (R) '/gpfs/bbp.cscs.ch/data/project/proj16/kumbhar/pramod_scratch/reframe_test/reframe/tutorial/example1.py'
  stage directory:   '/gpfs/bbp.cscs.ch/data/project/proj16/kumbhar/pramod_scratch/reframe_test/reframe/stage'
  output directory:  '/gpfs/bbp.cscs.ch/data/project/proj16/kumbhar/pramod_scratch/reframe_test/reframe/output'

[==========] Running 1 check(s)
[==========] Started on Mon Jun 29 09:58:33 2020

[----------] started processing Example1Test (Simple matrix-vector multiplication example)
[ RUN      ] Example1Test on bb5:login using PrgEnv-gnu
[ RUN      ] Example1Test on bb5:login using PrgEnv-intel
[ RUN      ] Example1Test on bb5:login using PrgEnv-pgi
[----------] finished processing Example1Test (Simple matrix-vector multiplication example)

[----------] waiting for spawned checks to finish
[       OK ] (1/3) Example1Test on bb5:login using PrgEnv-gnu [compile: 0.598s run: 0.930s total: 1.583s]
[       OK ] (2/3) Example1Test on bb5:login using PrgEnv-intel [compile: 0.527s run: 0.520s total: 1.069s]
[       OK ] (3/3) Example1Test on bb5:login using PrgEnv-pgi [compile: 0.201s run: 0.448s total: 0.671s]
[----------] all spawned checks have finished

[  PASSED  ] Ran 3 test case(s) from 1 check(s) (0 failure(s))
[==========] Finished on Mon Jun 29 09:58:35 2020
```

Run test on all partitions of BB5 using:

```bash
./bin/reframe -C config/bb5.py --system=bb5 -c tutorial/example1.py -r
[ReFrame Setup]
  version:           3.1-dev0 (rev: b2b3b6be)
  command:           './bin/reframe -C config/bb5.py --system=bb5 -c tutorial/example1.py -r'
  launched by:       kumbhar@bbpv1.epfl.ch
  working directory: '/gpfs/bbp.cscs.ch/data/project/proj16/kumbhar/pramod_scratch/reframe_test/reframe'
  settings file:     '/tmp/tmp1iy4me1f.py'
  check search path: (R) '/gpfs/bbp.cscs.ch/data/project/proj16/kumbhar/pramod_scratch/reframe_test/reframe/tutorial/example1.py'
  stage directory:   '/gpfs/bbp.cscs.ch/data/project/proj16/kumbhar/pramod_scratch/reframe_test/reframe/stage'
  output directory:  '/gpfs/bbp.cscs.ch/data/project/proj16/kumbhar/pramod_scratch/reframe_test/reframe/output'

[==========] Running 1 check(s)
[==========] Started on Mon Jun 29 10:03:17 2020

[----------] started processing Example1Test (Simple matrix-vector multiplication example)
[ RUN      ] Example1Test on bb5:login using PrgEnv-gnu
[ RUN      ] Example1Test on bb5:login using PrgEnv-intel
[ RUN      ] Example1Test on bb5:login using PrgEnv-pgi
[ RUN      ] Example1Test on bb5:knl using PrgEnv-gnu
[ RUN      ] Example1Test on bb5:knl using PrgEnv-intel
[ RUN      ] Example1Test on bb5:gpu using PrgEnv-gnu
[ RUN      ] Example1Test on bb5:gpu using PrgEnv-intel
[ RUN      ] Example1Test on bb5:gpu using PrgEnv-pgi
[ RUN      ] Example1Test on bb5:cpu using PrgEnv-gnu
[ RUN      ] Example1Test on bb5:cpu using PrgEnv-intel
[ RUN      ] Example1Test on bb5:p2 using PrgEnv-gnu
[ RUN      ] Example1Test on bb5:p2 using PrgEnv-intel
[----------] finished processing Example1Test (Simple matrix-vector multiplication example)

[----------] waiting for spawned checks to finish
[       OK ] ( 1/12) Example1Test on bb5:login using PrgEnv-pgi [compile: 0.125s run: 2.431s total: 3.659s]
[       OK ] ( 2/12) Example1Test on bb5:login using PrgEnv-gnu [compile: 0.127s run: 2.950s total: 4.197s]
[       OK ] ( 3/12) Example1Test on bb5:login using PrgEnv-intel [compile: 0.254s run: 4.864s total: 6.419s]
[       OK ] ( 4/12) Example1Test on bb5:gpu using PrgEnv-pgi [compile: 0.124s run: 6.771s total: 7.346s]
[       OK ] ( 5/12) Example1Test on bb5:gpu using PrgEnv-gnu [compile: 0.131s run: 7.051s total: 7.930s]
[       OK ] ( 6/12) Example1Test on bb5:gpu using PrgEnv-intel [compile: 0.229s run: 9.380s total: 10.052s]
[       OK ] ( 7/12) Example1Test on bb5:p2 using PrgEnv-gnu [compile: 0.130s run: 11.200s total: 11.354s]
[       OK ] ( 8/12) Example1Test on bb5:cpu using PrgEnv-gnu [compile: 0.127s run: 11.442s total: 11.888s]
[       OK ] ( 9/12) Example1Test on bb5:knl using PrgEnv-gnu [compile: 0.158s run: 12.456s total: 13.229s]
[       OK ] (10/12) Example1Test on bb5:p2 using PrgEnv-intel [compile: 0.222s run: 12.523s total: 12.773s]
[       OK ] (11/12) Example1Test on bb5:knl using PrgEnv-intel [compile: 0.227s run: 14.050s total: 14.605s]
[       OK ] (12/12) Example1Test on bb5:cpu using PrgEnv-intel [compile: 0.223s run: 13.782s total: 14.026s]
[----------] all spawned checks have finished

[  PASSED  ] Ran 12 test case(s) from 1 check(s) (0 failure(s))
[==========] Finished on Mon Jun 29 10:03:33 2020
```


## Getting ReFrame (Upstream)

You may install ReFrame directly from [PyPI](https://pypi.org/project/ReFrame-HPC/) through `pip`:

```bash
pip install reframe-hpc
```

ReFrame will be available in your PATH:

```bash
reframe -V
```

Alternatively, and especially if you want to contribute back to the framework, you may clone this repository:

```bash
git clone https://github.com/eth-cscs/reframe.git
cd reframe
./bin/reframe -V
```

Finally, you may access all previous versions of ReFrame [here](https://github.com/eth-cscs/reframe/releases).


## Documentation

You may find the official documentation of the latest release and the current master in the following links:

- [Latest release](https://reframe-hpc.readthedocs.io/en/stable)
- [Current master](https://reframe-hpc.readthedocs.io)


### Building the documentation locally

You may build the documentation of the master locally either with Python 2 or Python 3.
Here is how to do it:

```
pip install -r docs/requirements.txt
make -C docs latest
```

For viewing it, you may do the following:

```
cd docs/html
python -m http.server # or python -m SimpleHTTPServer for Python 2
```

The documentation is now up on [localhost:8000](http://localhost:8000), where you can navigate with your browser.


## Examples of Regression Tests

In the `cscs-checks/` folder, you can find realistic regression tests used for the CSCS systems that you can reuse and adapt to your system.
Notice that these tests are published as examples and may not run as-is in your system.
However, they can serve as a very good starting point for implementing your system tests in ReFrame.


## Contact

You can get in contact with the ReFrame community in the following ways:

### Mailing list

For keeping up with the latest news about ReFrame, posting questions and, generally getting in touch with other users and the developers, you may follow the mailing list: [reframe@sympa.cscs.ch](mailto:reframe@sympa.cscs.ch).

Only subscribers may send messages to the list.
To subscribe, please send an empty message to [reframe-subscribe@sympa.cscs.ch](mailto:reframe-subscribe@sympa.cscs.ch).

For unsubscribing, you may send an empty message to [reframe-unsubscribe@sympa.cscs.ch](mailto:reframe-unsubscribe@sympa.cscs.ch).

### Slack

You may also reach the community through Slack [here](https://reframe-slack.herokuapp.com).


## Contributing back

ReFrame is an open-source project and we welcome third-party contributions.
Check out our Contribution Guide [here](https://github.com/eth-cscs/reframe/wiki/contributing-to-reframe).
