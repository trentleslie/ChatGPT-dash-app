#import dependencies
from dash import Dash, dcc, html, Input, Output, State, callback_context
import dash_bootstrap_components as dbc
from api_key import api_key
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = api_key

def system_prompts():
    return  html.Div([
             html.H3('Select your writing genre:')
             , dbc.Row([
                dbc.Col(
                    dcc.Dropdown(id = 'sys-prompt', options=['Cover Letter', 'Blog Post', 'Academic Essay', 'Horror Story', 'Romance Novel']
                    , value='Cover Letter')
                , width=4)#end col 1
             , dbc.Col(
                    html.P('Sets the system level prompt to improve the style of the output.')
                    , width=6
                    )#end col 2          
             ])#end row 
         ])#end div

def output_style():
    return  html.Div([
             html.H3('Select your output style:')
             , dbc.Row([
                dbc.Col(
                    dcc.Dropdown(id = 'output-style', options=['Letter', 'Open', 'Outline', 'Paragraph', 'List']
                    , value='Letter')
                , width=4)#end col 1
             , dbc.Col(
                    html.P('Sets the style of output returned (outline, paragraph, or list)')
                    , width=6
                    )#end col 2          
             ])#end row 
         ])#end div

def text_areas():
    return html.Div([ 
            html.H3('Please enter the following information:')
            , html.Div([
                html.P('Role'),
                dbc.Input(id='role-input', type='text', placeholder='Enter role')
            ], className='mb-3'),
            html.Div([
                html.P('Company'),
                dbc.Input(id='company-input', type='text', placeholder='Enter company')
            ], className='mb-3'),
            html.Div([
                html.P('Job Description'),
                dbc.Input(id='job-description-input', type='text', placeholder='Enter job description')
            ], className='mb-3'),
            html.Div([
                html.P('Enter your prompt'),
                dbc.Textarea(id='my-input', size='lg', placeholder='Enter your text')
            ], className='mb-3'),
            dbc.Button("Generate Text", id="gen-button", className="me-2", n_clicks=0)
            ])

#instantiate dash
app = Dash(__name__
, external_stylesheets=[dbc.themes.SOLAR]
)#create layout

app.layout = html.Div([
        dbc.Container([
            html.H1('ChatGPT Writing Assitant')
            , html.Br()
            , system_prompts()
            , html.Br()
            , output_style()
            , html.Br()
            , text_areas()
            , html.Br()
            , html.H3('Output:')
            , html.Div(id='my-output')
        ]) #end container
  ]) #end div

@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='gen-button', component_property='n_clicks'),
    Input(component_id='sys-prompt', component_property='value'),
    Input(component_id='output-style', component_property='value'),
    State(component_id='my-input', component_property='value'),
    State(component_id='role-input', component_property='value'),
    State(component_id='company-input', component_property='value'),
    State(component_id='job-description-input', component_property='value')  
)
def update_output_div(gen, sp, os, input_value, role_input, company_input, job_description_input):
    #print(input_value) #debug
    
    #set text to sample
    text = "This is a \nsample"
    
    #listen for button clicks
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]

    #create system prompt logic
    if sp == 'Cover Letter':
        system_prompt = f'''You are a world class cover letter writer that wants to produce a cover letter for the role of {role_input} at {company_input} that will get you the job. 
                                You have been given the following job description to work with: "{job_description_input}".
                                Your resume is as follows: 
                                "Analytical and results-driven professional with over 10 years of data analytics experience and skilled at using statistical analysis and data visualization to uncover valuable insights and drive informed decision-making.
                                Stellar record of conducting data analysis and visualization through projects, including identifying response biomarkers in lung and urothelial carcinoma datasets, and investigating composite biomarkers for Merkel Cell Carcinoma. Demonstrated expertise in machine learning with a proven track record of developing and applying advanced computational techniques to solve complex biological problems. Extensive knowledge of scientific techniques including preparation, characterization, testing, evaluation, data analysis, and collection. Well-versed in leading and coaching teams and the ability to establish professional development programs to improve staff performance. Proven experience in analyzing bulk and single-cell RNA-seq, functional enrichment, and deconvolution.  Competency in utilizing cloud computing, high-performance computing, and Linux/Ubuntu operating systems.
                                Areas of Expertise
                                Bioinformatics / Machine Learning
                                Biomarker Discovery / Validation
                                Data Analysis / Interpretation
                                Project / Program Management
                                Continuous Improvement / Innovation
                                Report Writing / Presentation
                                Quality Control / Assurance
                                Gene Expression Profiling
                                Team Development / Leadership
                                Statistical Analysis / Data Mining
                                Problem Solver / Decision Maker
                                Research / Development

                                Career Experience

                                Bioinformatics Contractor | EMD Serono R&D Institute, Billerica, MA (Remote)	2021 – 2022
                                Utilized RShiny to extract, process, and load RNAseq data and full exome sequencing profiles from four phase I-III UC trials, including TCGA. Identified loss-of-function mutations to validate the mutation status of one gene as a biomarker for resistance of the avelumab maintenance in the internal UC cohort.
                                Conducted research, analyzed, and disproved the avelumab combination hypothesis for two major DNA damage response genes.

                                Key Projects

                                RShiny infrastructure for visualizing & analyzing clinical data & molecular profiles for Urothelial carcinoma patients. 
                                Extracted, processed, and imported RNAseq data and whole exome sequencing (WES) profiles of four multiple phase I-III UC trials into RShiny integrated analysis app, including TCGA.
                                Created and implemented configuration for R6 classes to import clinical information, genomic data, and efficacy association information.
                                Identifying response biomarkers & combination rationale to overcome avelumab resistance in Lung & UC datasets.
                                Verified mutation status of gene as a biomarker for avelumab maintenance resistance in internal UC cohort by defining loss-of-function mutations in personals-generated mutation calling output from tumour-only sequencing.
                                Aided in creating a synthetic comparator for a combination trial by assessing existing phase III monotherapy datasets and real-world evidence data from TEMPUS.
                                Utilized Kaplan-Meier and forest plots to validate the patient stratification hypothesis through the development of univariate and multivariate survival models.
                                Rejected the avelumab combination hypothesis for two significant DNA damage response (DDR) genes
                                Understanding biomarkers of response & resistance to Merkel Cell Carcinoma for patients treated with avelumab in 1L and 2L
                                Integrated omics data such as PD-L1/CD8 status from manual & digital pathology, gene expression, gene signatures, somatic mutations, mutational signatures, and tumour mutation burden to study composite biomarkers.
                                Verified a treatment resistance hypothesis by utilizing a publicly accessible scRNAseq dataset for tSNE clustering and immune cell type annotation
                                Quality Manager | MadTree Brewing, Cincinnati, OH	2014 – 2021
                                Managed a cross-functional team to develop, execute, and maintain quality management systems/processes. Drove initiatives for continuous improvement to maximize effectiveness and guarantee reliable product output. Chaired and organized regular team meetings to inform and update staff regarding progress, challenges, and opportunities. Conducted research and presented outcomes at various conferences, including delivering presentations, organizing and moderating panel discussions, and participating in roundtable discussions. Acted as a chair of the American Society of Brewing Chemists (ASBC) Technical Committee and Craft Beer Subcommittee while leading Committee meetings and the development and launch of the ASBC Sampling Plans.
                                Six Sigma project:  Kolsch Yeast Counts: Improving Reliability of Representative Samples to improve beer consistency
                                Improved random sampling and counting of yeast to provide a more accurate pitch of yeast into the wort.
                                Utilized Six Sigma methodology and design of experiments (DOE), resulting in enhancing brewhouse efficiency for the house IPA brand by 4%.
                                Improved data gathering processes and optimized team performance by designing and introducing 14 inductive automation ignition data input dashboards.
                                Minimized the number of test batches for new brands by 50% through the execution of mixture experiments for recipe development. 
                                Conceptualized and established a professional development program for staff, resulting in the promotion of four team members to supervisory positions within the organization.

                                Additional Experience

                                Graduate Student, Teaching & Research Assistant | University of Cincinnati, Cincinnati, OH, 2011 – 2014


                                Education

                                MS, Biological Sciences | University of Cincinnati, Cincinnati, OH, 2013
                                BS, Aerospace Engineering | Saint Louis University, St. Louis, MO, 2006


                                Licenses & Certifications

                                Data Science Certificate – Springboard (Online), 2021
                                    Six Sigma Black Belt Certification – Xavier Leadership Center, Cincinnati, OH  

                                Publications & Presentations

                                Genetic, transcriptional, and immunological biomarker analyses to investigate the biology of metastatic Merkel cell carcinoma and outcomes with avelumab treatment in the phase 2 JAVELIN Merkel 200 trial." D’Angelo S.P et al.  (In preparation)
                                "De novo assembly and annotation of the transcriptome of the agricultural weed Ipomoea purpurea uncovers gene expression changes associated with herbicide resistance." Leslie, Trent, and Regina S. Baucom. G3: Genes, Genomes, Genetics 4.10 (2014): 2035-2047. http://bit.ly/TL_Publication/. 
                                You Can’t Always Get What You Want - Use of Design of Experiments (DOE) to Optimize Dry Hop Mixtures for Aroma and Flavor, ASBC Virtual Presentation (co-author) 2021; https://bit.ly/ASBC_Talk2/. 
                                But Sometimes You Get What You Need - Using R to Optimize Dry Hop Mixtures for Aroma and Flavor, American Society of Brewing Chemists (ASBC) Virtual Presentation 2021; https://bit.ly/ASBC_Talk3/. 
                                Standardized Data Collection with ASBC Sampling Plan, ASBC Webinar 2021;  http://bit.ly/ASBC_Webinar3/. 
                                Data Collection, Organization, and Integration​​​​​​​​​, ASBC Webinar 2020; http://bit.ly/ASBC_Webinar2/. 
                                Exploration of the flavor space - Using design of experiments (DOE) to model the sensory impact of post-fermentation additions, ASBC Presentation (co-author) 2019; http://bit.ly/ASBC_Talk1/.
                                From Bytes to BeeR - Leveraging the Statistical Programming Language R in Brewing Data Science, ASBC Conference Workshop 2019; http://bit.ly/ASBC_Workshop1/.
                                Five Critical Quality Checks for Small Breweries​, ASBC Webinar 2017; http://bit.ly/ASBC_Webinar1/.


                                Technical Proficiencies 

                                Data Analysis:
                                Bulk & single cell RNASeq | whole-exome DNA sequencing | functional enrichment (Gene Ontology, GSEA, CAMERA) | deconvolution (xCell, Cibersort) | de-novo transcriptome assembly (SOAPdenovo-Trans) | trichromatic | Bowtie2 | BLAST | samtools | Primer3 | H&E and PD-L1/CD8 IHC output from PathAI & Definiens
                                Languages:
                                R & Bioconductor (DESeq2 | edgeR, survival | Seurat | tidyverse | fGSEA | limma | shiny | markdown) | Python (Jupyter | Pandas | NumPy | Scikit-Learn | PySpark | Keras | Tensorflow) | SQL (PostgreSQL)
                                Data Visualization:
                                Statistics & ML:

                                Other Skills:
                                ggplot2 | plotly | survminer | ComplexHeatmap | Cytoscape | MatplotLib | Seaborn | RShiny
                                Design of Experiments (DOE) | Statistical Process Control | Hypothesis Testing | Regression | Classification | kNN | Random Forest | K-Means Clustering | Neural Networks
                                Cloud computing (AWS) | High-performance computing (PBS Cluster Computing Environment) | Operating system (Linux/Ubuntu, Windows) | Version control (GitHub/GitLab)"'''
    elif sp == 'Blog Post':
        system_prompt = 'You are a world class bioinformatics tutorial blogger that wants to produce a blog post that will get you recognized. Your style is similar to that of David Sedaris, writing in a humorous, self-deprecating style that is also reflective. Produce content with code snippets and suggestions for pictures or screen shots.'
    elif sp == 'Academic Essay':
        system_prompt = 'You are a world class academic professor and a world class technical writer that wants to produce coherent academic essays. Produce content step by step.'
    elif sp == 'Horror Story':
        system_prompt = 'You are a world class horror author with a style similar to Stephen King and Anne Rice. Generate content that contains logical twists and builds suspense. Produce content step by step.'
    else:
        system_prompt = 'You are a world class romance novelist with a style similar to Nora Roberts and Jane Austen. Generate content that is tantilizing, lustrious, and very erotic. Produce content step by step.'

   #create output style logic
    if os == 'Letter':
        style = 'Respond with a cover letter no longer than 500 words and no more than 5 paragraphs.'
    elif os == 'Open':
        style = 'Respond with an open ended response no shorter than 500 words'
    elif os == 'Outline':
        style = 'Respond with an outline no longer than 500 words'
    elif os == 'Paragraph':
        style = 'Respond with at least one paragraph. Output at least 200 words.'
    else:
        style = 'Respond with a top 15 list. Output is limited to 150 words.'
    
    #build messages payload
    messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": style},
            {"role": "assistant", "content": "On what topic?"},
            {"role": "user", "content": input_value}
        ]

    
    #button logic to submit to chatGPT API
    if 'gen-button' in changed_id:
        print(input_value)
        if input_value is None or input_value == "":
            input_value = ""
            text = html.P('hello <br> this is </br> a <br> test ')

        else:
            print(input_value)
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature = 0.8,
                top_p = 1, 
                presence_penalty = 0.5,
                frequency_penalty = 0.4            
            )
            text = (response['choices'][0]['message']['content'])

    return html.P(text, style = {'white-space': 'pre-wrap'})

#run app server
if __name__ == '__main__':
    app.run_server(debug=True)
