# ai-stroke-outcomes

### Repo Structure
```
├── README.md
├── caller.py
├── aux_dtypes.py
├── ex_clinical.csv
├── ex_idf.csv
├── ex_embedding.csv
├── dist
│   ├── embed
│   └── embed.exe
│   ├── reconstruct
│   └── reconstruct.exe
│   ├── predict_los
│   └── predict_los.exe
│   ├── predict_mrs
│   └── predict_mrs.exe
```

### Usage
First download the model executables from [Google Drive](https://drive.google.com/drive/folders/1GqAq8Y4tsObN5Q2lPpvnA50KQw0BxGMT?usp=sharing) and unzip them into a dist folder to match the repo structure above. 

* To embed a 3D DWI MRI (ie AE encoder): 
  * Follow the preprocessing steps including template matching and brain mask normalization detailed in [Liu et al](https://www.nature.com/articles/s41597-023-02457-9). 
  * Edit caller.py to call function `call_embed` in  main body of code
  * ``` python ./caller.py --image "<full path to file>.nii.gz"```
  * This will create a csv file with three latent space embeddings, one for each training fold\
  
* To reconstruct an image from an embedded latent space vector (ie AE decoder): 
  * Edit caller.py to take in the .csv file created above (example: ex_embedding.csv) 
  * Call function `call_reconstruct` in  main body of code
  * ``` python ./caller.py```
  * This will create 3D .nrrd files in the specified directory for each model fold
  
* To predict length of stay (LOS) > 8 days using latent space embeddings:
  * Edit caller.py to take in .csv files containing the latent space embedding of the DWI, the clinical metadata, and the image derived features (IDF). 
    * Call function `call_los_prediction` in  main body of code
    * Clinical and IDF data should follow the order, naming conventions, and data types outlined in aux_dtypes.xlsx
    * Example clinical and IDF files are provided (ex_clinical.csv, ex_idf.csv)
    * The model can be called with any of the following combinations: 
      * embedding.csv
      * embedding.csv + clinical.csv
      * embedding.csv + idf.csv
      * embedding.csv + clinical.csv + idf.csv
  * ``` python ./caller.py```
  * This will print the binary classifier prediction (prior to thresholding) from each fold of the model
* 
* To predict 90-day modified Rankin scale > 2 using latent space embeddings:
  * Edit caller.py to take in .csv files containing the latent space embedding of the DWI, the clinical metadata, and the image derived features (IDF). 
    * Call function `call_mrs_prediction` in  main body of code
    * Clinical and IDF data should follow the order, naming conventions, and data types outlined in aux_dtypes.xlsx
    * Example clinical and IDF files are provided (ex_clinical.csv, ex_idf.csv)
    * The model can be called with any of the following combinations: 
      * embedding.csv
      * embedding.csv + clinical.csv
      * embedding.csv + idf.csv
      * embedding.csv + clinical.csv + idf.csv
  * ``` python ./caller.py```
  * This will print the binary classifier prediction (prior to thresholding) from each fold of the model

### Copyright
(c) University of Michigan, 2025

This software is licensed under the Polyform Non-Commercial License 1.0.0. You may use, modify, and distribute this software for non-commercial purposes only, as outlined in the license. Commercial use, as defined by the license, is not permitted.

For more information about the terms and conditions of this license, please see the full license text at: https://polyformproject.org/licenses/noncommercial/1.0.0/

By using, modifying, or distributing the software, you agree to the terms and conditions of the Polyform Non-Commercial License 1.0.0 and acknowledge that you have read and understood them.

### Additional Disclosures

- This software is provided "as-is," without any warranty of any kind, either express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement.
- In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

Should you have any questions about this license or the permitted uses, please contact innovationpartnerships@umich.edu.