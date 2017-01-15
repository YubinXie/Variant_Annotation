library(splitstackshape)
annotate1.data <- read.csv(file='~/tools/annovar/MIdataSplit.hg19_multianno.csv')
avsnp.data <- read.csv(file='~/tools/annovar/MIdataSplitAv.hg19_multianno.csv')[,6]
count.case <- read.csv(file='~/tools/annovar/MIGen_Case_Split_Count.frq.count',sep = "\t", header = FALSE)[-1,]
count.control <- read.csv(file='~/tools/annovar/MIGen_Control_Split_Count.frq.count',sep = "\t", header = FALSE)[-1,]
count.case <- cSplit(indt =count.case, splitCols = "V6", sep=":",drop = TRUE)
count.control <- cSplit(indt=count.control, splitCols = "V6", sep=":",drop = TRUE)
exonconstarinscore.missense.data <-read.csv(file='~/tools/annovar/mySPlitMIdata.avinput.hg19_multianno.txt',sep = "\t")[,6]
exonconstarinscore.missense.data <-gsub("Name=","",exonconstarinscore.missense.data)
RNAseqGeneExpression.data <-read.csv(file='~/MIdata_heartexpression.txt',sep = "\t",header = F)[,6]
annotate.data <- cbind(annotate1.data[,1:5],avsnp.data,count.case[,4], count.case[,7],count.control[,7],exonconstarinscore.missense.data,RNAseqGeneExpression.data,annotate1.data[,6:55])
colnames(annotate.data)[6]<-"avsnp147"
colnames(annotate.data)[7]<-"Chr_Num"
colnames(annotate.data)[8]<-"Case_Num"
colnames(annotate.data)[9]<-"Control_Num"
colnames(annotate.data)[10]<-"ExonConScore_Missense"
colnames(annotate.data)[11]<-"GeneExpression"
save(annotate.data,file="~/R/Annotation/MIdataAnnotationV5.RData")
