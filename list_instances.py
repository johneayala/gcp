import argparse
import os
import time

import googleapiclient.discovery
from six.moves import input


def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items'] if 'items' in result else None


def main(project, zone):
    compute = googleapiclient.discovery.build('compute', 'v1')

    instances = list_instances(compute, project, zone)

    print('Instances in project %s and zone %s:' % (project, zone))
    for instance in instances:
        print(' - ' + instance['name'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('project_id', help='Your Google Cloud project ID.')
    parser.add_argument(
            '--zone',
            default='us-west2-a',
            help='Compute Engine zone to deploy to.')

    args = parser.parse_args()

    main(args.project_id, args.zone)

