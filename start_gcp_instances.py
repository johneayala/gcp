import argparse
import os
import time
import pprint

import googleapiclient.discovery
from six.moves import input



def main(project, zone, name):
    compute = googleapiclient.discovery.build('compute', 'v1')

    print('Starting instance: %s - project: %s - zone: %s' % (name, project, zone))
    request=compute.instances().start(project=project, zone=zone, instance=name)
    response=request.execute()
    pprint.pprint(response)


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
parser.add_argument('inputfile', help='File containing Google Cloud instance names.')
args = parser.parse_args()

#print('zone is:' + args.zone)
#print('project is:' + args.projectid)
#print('input file is:' + args.inputfile)

with open(args.inputfile) as fp:
    for line in fp:
        line=line.rstrip('\n')
        if not line:
            continue
        else:
#            print(line)
            instname=line
            main(args.projectid, args.zone, instname)

