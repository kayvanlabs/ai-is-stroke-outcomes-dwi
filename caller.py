import subprocess
import argparse
import os
import sys

def call_embed(image_path, out_dir):
    # Command to run the executable
    fn = './dist/embed.exe' if sys.platform.startswith('win') else './dist/embed'
    command = [
        fn  # Use 'predictor' on Linux
        ,'--image', image_path  # Path to the input 3D image ending in .nii.gz
        ,'--out_dir', out_dir  # Path to where output should be saved
        # ,'--out_fn', 'embedding.csv'  # Desired filename of the embedding file. Must end in .csv (Default embedding.csv)
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        print("Embedding:", result.stdout.strip())
    else:
        print("Error:", result.stderr)

def call_reconstruct(embed_path, out_dir):
    # Command to run the executable
    fn = './dist/reconstruct.exe' if sys.platform.startswith('win') else './dist/reconstruct'
    command = [
        fn  # Use 'predictor' on Linux
        ,'--embedding', embed_path  # Path to the input embedding file ending in .csv
        ,'--out_dir', out_dir  # Path to where output should be saved
        # ,'--out_fn', 'reconstruct'  # Desired filename prefix of the reconstructed image (Default reconstruct)
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        print("Error:", result.stderr)

def call_los_prediction(embed_path, clinical_path=None, idf_path=None):
    # Command to run the executable
    fn = './dist/predict_los.exe' if sys.platform.startswith('win') else './dist/predict_los'
    command = [
        fn  # Use 'predictor' on Linux
        ,'--embedding', embed_path  # Path to the input embedding file ending in .csv
        ,'--clinical', clinical_path  # Path to the corresponding clinical data file ending in .csv
        , '--idf', idf_path # Path to the corresponding image derived features file ending in .csv
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        print(result.stdout.strip())
    else:
        print("Error:", result.stderr)


def call_mrs_prediction(embed_path, clinical_path=None, idf_path=None):
    # Command to run the executable
    fn = './dist/predict_mrs.exe' if sys.platform.startswith('win') else './dist/predict_mrs'
    command = [
        fn  # Use 'predictor' on Linux
        ,'--embedding', embed_path  # Path to the input embedding file ending in .csv
        ,'--clinical', clinical_path  # Path to the corresponding clinical data file ending in .csv
        , '--idf', idf_path # Path to the corresponding image derived features file ending in .csv
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        print(result.stdout.strip())
    else:
        print("Error:", result.stderr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', required=False, help="Full path to the input 3D DWI MRI image ending in .nii.gz")
    parser.add_argument('--out_dir', required=False, help="Path to where output should be saved", default='output')
    args = parser.parse_args()

    ### Make embedding directory
    out_dir_embed = os.path.join(args.out_dir, 'embeddings')
    # if not os.path.exists(out_dir_embed):
    #     os.makedirs(out_dir_embed)

    ### Encode image
    # call_embed(args.image, out_dir_embed)


    ### Make reconstruction directory
    # out_dir_rec = os.path.join(args.out_dir, 'reconstructions')
    # if not os.path.exists(out_dir_rec):
    #     os.makedirs(out_dir_rec)

    ### Reconstruct image
    # call_reconstruct('ex_embedding.csv', out_dir_rec)


    ### Predict los > 8 days
    call_los_prediction('ex_embedding.csv','ex_clinical.csv', 'ex_idf.csv')

    ### Predict mRS > 2
    call_mrs_prediction('ex_embedding.csv','ex_clinical.csv', 'ex_idf.csv')


