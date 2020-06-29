#
# Minimal settings for ReFrame tutorial on Piz Daint
#


class ReframeSettings:
    job_poll_intervals = [1, 2, 3]
    job_submit_timeout = 60
    checks_path = ['checks/']
    checks_path_recurse = True
    site_configuration = {
        'systems': {
            'bb5': {
                'descr': 'Blue Brain 5',
                'hostnames': ['bbpv1', 'bbpv2'],
                'modules_system': 'tmod',
                'partitions': {
                    'login': {
                        'scheduler': 'local',
                        'modules': [],
                        'access':  [],
                        'environs': ['PrgEnv-gnu', 'PrgEnv-intel', 'PrgEnv-pgi'],
                        'descr': 'Login nodes',
                        'max_jobs': 4
                    },

                    'knl': {
                        'scheduler': 'nativeslurm',
                        'modules': [],
                        'access':  ['--constraint=knl', '--account=proj16'],
                        'environs': ['PrgEnv-gnu', 'PrgEnv-intel'],
                        'container_platforms': {},
                        'descr': 'UC1 (Xeon Phi)',
                        'max_jobs': 120
                    },

                    'gpu': {
                        'scheduler': 'nativeslurm',
                        'modules': [],
                        'access':  ['--constraint=volta', '--account=proj16'],
                        'environs': ['PrgEnv-gnu', 'PrgEnv-intel', 'PrgEnv-pgi'],
                        'container_platforms': {},
                        'descr': 'UC2 (Skylake/V100)',
                        'max_jobs': 7
                    },

                    'cpu': {
                        'scheduler': 'nativeslurm',
                        'modules': [],
                        'access':  ['--constraint=cpu', '--account=proj16'],
                        'environs': ['PrgEnv-gnu', 'PrgEnv-intel'],
                        'container_platforms': {},
                        'descr': 'UC3 (Skylake)',
                        'max_jobs': 207
                    },

                    'p2': {
                        'scheduler': 'nativeslurm',
                        'modules': [],
                        'access':  ['--account=proj95'],
                        'environs': ['PrgEnv-gnu', 'PrgEnv-intel'],
                        'container_platforms': {},
                        'descr': 'UC4 (Skylake)',
                        'max_jobs': 100
                    }

                }
            }
        },

        'environments': {
            '*': {
                'PrgEnv-gnu': {
                    'type': 'ProgEnvironment',
                    'modules': ['unstable', 'gcc/8.3.0'],
                },

                'PrgEnv-intel': {
                    'type': 'ProgEnvironment',
                    'modules': ['unstable', 'intel/19.0.4'],
                },

                'PrgEnv-pgi': {
                    'type': 'ProgEnvironment',
                    'modules': ['unstable', 'pgi/19.10'],
                }
            }
        }
    }

    logging_config = {
        'level': 'DEBUG',
        'handlers': [
            {
                'type': 'file',
                'name': 'reframe.log',
                'level': 'DEBUG',
                'format': '[%(asctime)s] %(levelname)s: '
                          '%(check_name)s: %(message)s',
                'append': False,
            },

            # Output handling
            {
                'type': 'stream',
                'name': 'stdout',
                'level': 'INFO',
                'format': '%(message)s'
            },
            {
                'type': 'file',
                'name': 'reframe.out',
                'level': 'INFO',
                'format': '%(message)s',
                'append': False,
            }
        ]
    }

    perf_logging_config = {
        'level': 'DEBUG',
        'handlers': [
            {
                'type': 'filelog',
                'prefix': '%(check_system)s/%(check_partition)s',
                'level': 'INFO',
                'format': (
                    '%(asctime)s|reframe %(version)s|'
                    '%(check_info)s|jobid=%(check_jobid)s|'
                    '%(check_perf_var)s=%(check_perf_value)s|'
                    'ref=%(check_perf_ref)s '
                    '(l=%(check_perf_lower_thres)s, '
                    'u=%(check_perf_upper_thres)s)'
                ),
                'append': True
            }
        ]
    }

settings = ReframeSettings()
