# EDA Pipeline

## Visit the [Trello](https://trello.com/invite/b/oD8SWoh2/ATTIa54335873a4277497cf67c48786217e4FE1374C0/ece34-senior-design-group) for more information


**Requires**:

- Access to xunil
- Access to Synopsys install


**Steps**:

1. Install Prereuisites: 

   - OpenROAD
      1. ```
         git clone --recursive https://github.com/The-OpenROAD-Project/OpenROAD-flow-scripts.git 
         ```
      2. Follow this guide:
      3. **MAKE SURE YOU EDIT OpenROAD_pipeline.py TO REFLECT OPENROAD-flow-scripts' PATH**
2. Clone [eda-pipeline](https://gitlab.com/senior-design-g34/eda-pipeline/-/tree/main/ "‌").
   1. ```
      git clone git@gitlab.com:senior-design-g34/eda-pipeline.git
      cd eda-pipeline
      ```
   2. ```
      source sensei
      ```   
3. Run eda-pipeline.py
   1. ```
      python3 eda-pipeline.py
      ```
4. Finally, choose 
   - Design Name 
   - Process type: Single or Bulk 
   - And choose your tool!
   
   **or**
   
   - Create your own custom .json file and put it in Custom_Configs!











