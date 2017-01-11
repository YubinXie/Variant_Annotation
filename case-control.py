import vcf
import subprocess
#import sys, optparse

######## This part can be comstumed###########
#HeaderFile is a VCF file that contains your sample name information, no variants and sample information required#
HeaderFile="../Files/example.vcf"
#InputFileName is a VCF file that contains your sample name information, no variants and sample information required#
InputFileName = "MIGen_ExS_28K.v6.ATVB_NoDup.vcf.gz"
#CasePattern is the string feature that is only contained in case sample name# 
CasePattern="A"
#ControlPattern is the string feature that is only contained in control sample name# 
ControlPattern="B"




vcf_reader = vcf.Reader(open(HeaderFile, 'r'))
#record = next(vcf_reader)
SampleNameList=vcf_reader.samples
Commend = ""
#To count the case sample number
NumberPlus = 0
#To count the control sample number
NumberMinus = 0
NumberZero = 0
Case = []
CaseString = ""
Control=[]
ControlString=""
for CasePattern in SampleNameList:
	if "A" in sample:
		Commend=Commend+"+"
		Case.append(sample)
		NumberPlus=NumberPlus+1
		CaseString=CaseString+sample+","
	elif "B" in sample:
		Commend=Commend+"-"
		Control.append(sample)
		NumberMinus=NumberMinus+1
		ControlString=ControlString+sample+","
	else:
		Commend=Commend+"0"
		NumberZero=NumberZero+1
print Commend
print NumberPlus, NumberMinus, NumberZero,Case,Control
print CaseString
print ControlString

CaseCommendLine="bcftools view -s " + CaseString + " " + InputFileName + " | bgzip -c > " + InputFileName + "_Case.vcf.gz"
ControlCommendLine="bcftools view -s " + ControlString + " " + InputFileName + " | bgzip -c > " + InputFileName + "_Control.vcf.gz"
CommendLine= CaseCommendLine + " && " + ControlCommendLine

subprocess.Popen(CommendLine,shell=True)
