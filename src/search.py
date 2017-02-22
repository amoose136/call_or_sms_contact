import sys, os, plistlib as pl
import workflow
from workflow import Workflow, ICON_INFO
from workflow.background import run_in_background, is_running
from plistlib import readPlist

def main(wf):
	wf.send_feedback()

if __name__ == '__main__':
	wf = Workflow(capture_args=True)
	log=wf.logger
	wf.magic_prefix='wf:'
	sys.exit(wf.run(main))