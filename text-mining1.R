#########################
#
#author: alvaroof90
#date: monday 22th August 2016
#script: import dict.csv (generated through a python script in this very same folder) and 
#analyses it using tm package and pther functionalities
#
#########################

library(tm)
library(SnowballC)

raw_text <- read.csv("dict.csv", header = FALSE, stringsAsFactors = FALSE)
corpus <- Corpus(VectorSource((data$V2))) #define corpus with the text
corpus <- tm_map(corpus, tolower) #to lowercase
corpus = tm_map(corpus, PlainTextDocument)
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, removeWords, c(stopwords("english")))
frequencies <- DocumentTermMatrix(corpus)
freqmat <- as.matrix(inspect(frequencies)) #inspecting the frequency matrix

wordcount <- apply(freqmat, 2, sum)
