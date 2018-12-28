import argparse
import os
import time

import googleapiclient.discovery
from six.moves import input



def main(project, zone, name):
    compute = googleapiclient.discovery.build('compute', 'v1')

    print('Starting instance: %s - project: %s - zone: %s' % (name, project, zone))
    compute.instances().start(project=project, zone=zone, instance=name).execute()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
	    '--projectid',
	    default='none',
	    help='Your Google Cloud project ID.')
    parser.add_argument(
            '--zone',
            default='us-west2-a',
            help='Compute Engine zone to deploy to.')
    parser.add_argument('name', help='Your Google Cloud instance name.')

    args = parser.parse_args()

    main(args.projectid, args.zone, args.name)

