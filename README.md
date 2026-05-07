# AST424-Variable-star-classification-project

The automatic classification of periodic variable stars is of immense value for many reasons, including 
finding standard candles, determining stellar properties accurately, and studying stellar life cycles. Ad
ditionally, missions like TESS and Gaia, which are unified in the MMU dataset, have provided millions 
of data points to study them. However, with this wealth of information comes the need to classify the 
different variable star types quickly. This project implements a machine learning approach to address 
this challenge. We developed a TESS processing pipeline that utilizes Lomb-Scargle periodograms to 
automatically extract periodicity features and filter for variability. These features are then used to 
manually classify the stars and feed the data to the program's training set. Our results demonstrate a 
functional feature extraction pipeline and a Random Forest classifier capable of distinguishing variable 
types, providing a scalable framework for analyzing the MMU dataset. Initial testing with a small 
data set of about 150 yielded a 63% accuracy. Expanding the training set to 688 and implementing 
rigorous data curation yielded a significantly improved accuracy of 76.81%.
