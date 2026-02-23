# SQLUser.PA_AdmLab

**Schema:** SQLUser
**Columnas:** 155
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALB_PAADM_ParRef | bigint | PK |  | NO | Des Ref to PAADM |
| ALB_AnaestUsed_DR | bigint |  | FK | SI | AnaestUsed Des Ref to ORCAnaMeth |
| ALB_AntenatalSteroids_DR | bigint |  | FK | SI | Des Ref Antenatal Steroids |
| ALB_BloodLoss | double |  |  | SI | Blood Loss |
| ALB_CertOfGestation_DR | bigint |  | FK | SI | Des Ref Certainty Of Gestation |
| ALB_CervixDate | date |  |  | SI | Cervix Expand Date |
| ALB_CervixTime | time |  |  | SI | Cervix Expand Time |
| ALB_Childsub | numeric |  |  | NO | Childsub |
| ALB_CordLength | double |  |  | SI | Cord Length |
| ALB_DegreeLaceration_DR | bigint |  | FK | SI | Degree of Laceration Des Ref to PACLacerDeg |
| ALB_DelivDate | date |  |  | SI | Delivery Date |
| ALB_DelivMethod_DR | bigint |  | FK | SI | Delivery Method |
| ALB_DelivTime | time |  |  | SI | Delivery Time |
| ALB_DeliveryDoctor_DR | varchar |  | FK | SI | ALB_DeliveryDoctor_DR |
| ALB_DeliveryNurse_DR | varchar |  | FK | SI | DeliveryNurse Des Ref to CTCP |
| ALB_DeliveryType_DR | bigint |  | FK | SI | Des Ref DeliveryType |
| ALB_Duration_Labour | time |  |  | SI | Duration of Labour |
| ALB_EpisType_DR | bigint |  | FK | SI | Episiotomy Type Des Ref to PACEpisType |
| ALB_Gestation | double |  |  | SI | Gestation In No Of Weeks |
| ALB_Gestation_Days | double |  |  | SI | Gestation Period in Days |
| ALB_IndicOperDeliv_DR | bigint |  | FK | SI | Des Ref ICDDx |
| ALB_Interval_Contractions | double |  |  | SI | Interval between Contractions |
| ALB_LabourDate | date |  |  | SI | Labour Date |
| ALB_LabourIntens_DR | bigint |  | FK | SI | Not Currently Used |
| ALB_LabourMethod_DR | bigint |  | FK | SI | Des Ref to LBMTH |
| ALB_LabourStartTime | time |  |  | SI | Labour start Time |
| ALB_LocationLaceration_DR | bigint |  | FK | SI | Location of Laceration Des Ref to PacLacLoc |
| ALB_MostSeniorDoc_DR | bigint |  | FK | SI | Des Ref CareProvType |
| ALB_MostSeniorMidwifePresent | bigint |  |  | SI | Des Ref CareProvType |
| ALB_NumberOfNewborn | double |  |  | SI | No Of Newborn (Should be computed from ADMNB) |
| ALB_PlacDelivType_DR | bigint |  | FK | SI | PlacDelivType Des Ref to PacPlacDelType |
| ALB_PlacentaCond_DR | bigint |  | FK | SI | Placenta Condition Des Ref to PacPlacCond |
| ALB_Placenta_Date | date |  |  | SI | Date Placenta was Delivered |
| ALB_Placenta_Time | time |  |  | SI | Time Placenta was Delivered |
| ALB_Placenta_Weight | double |  |  | SI | Placenta Weight |
| ALB_PostNatProb_DR | bigint |  | FK | SI | Post Natal Problem Des Ref to PacPosNatProb |
| ALB_Remarks | varchar |  |  | SI | Remarks |
| ALB_RowId | varchar |  |  | NO | - |
| ALB_RuptureDate | date |  |  | SI | Rupture Date of Amniotic Membrane |
| ALB_RuptureTime | time |  |  | SI | Rupture Time of Amniotic Membrane |
| Q01 | - |  |  | SI | Step 1 - Diagnosis: Does the child have a diagnosi... |
| Q02 | - |  |  | SI | Step 2 - Nutritional intake: What is the child’s n... |
| Q03 | - |  |  | SI | Step 3 - Weight and height: Use a growth chart or ... |
| Q04 | - |  |  | SI | STAMP care plan note |
| Q05 | - |  |  | SI | Care plan |
| Q06 | - |  |  | SI | Use management guidelines and/or local nutrition p... |
| Q07 | - |  |  | SI | High risk care plan |
| Q08 | - |  |  | SI | • Take action |
| Q09 | - |  |  | SI | • Refer the child to a dietitian, nutritional supp... |
| Q10 | - |  |  | SI | • Monitor as per care plan |
| Q11 | - |  |  | SI | Medium risk care plan |
| Q12 | - |  |  | SI | • Monitor the child's nuttritional intake for 3 da... |
| Q13 | - |  |  | SI | • Repeat the STAMP screening after 3 days |
| Q14 | - |  |  | SI | • Amend care plan as required |
| Q15 | - |  |  | SI | Low risk rare plan |
| Q16 | - |  |  | SI | • Continue routine clinical care |
| Q17 | - |  |  | SI | • Repeat STAMP screening weekly while the child is... |
| Q18 | - |  |  | SI | • Amend care plan as required |
| Q19 | - |  |  | SI | Guidelines to determine the nutritional implicatio... |
| Q20 | - |  |  | SI | Definite nutritional implications |
| Q21 | - |  |  | SI | • Bowel failure, intractable diarrhea |
| Q22 | - |  |  | SI | • Burns and major trauma |
| Q23 | - |  |  | SI | • Crohn's disease |
| Q24 | - |  |  | SI | • Cystic fibrosis |
| Q25 | - |  |  | SI | • Dysphagia |
| Q26 | - |  |  | SI | • Liver disease |
| Q27 | - |  |  | SI | • Major surgery |
| Q28 | - |  |  | SI | • Multiple food allergies / intolerances |
| Q29 | - |  |  | SI | • Oncology on active treatment |
| Q30 | - |  |  | SI | • Renal disease / failure |
| Q31 | - |  |  | SI | • Inborn errors of metabolism |
| Q32 | - |  |  | SI | Possible nutritional implications |
| Q33 | - |  |  | SI | • Behavioural eating problems |
| Q34 | - |  |  | SI | • Cardiology |
| Q35 | - |  |  | SI | • Cerebral palsy |
| Q36 | - |  |  | SI | • Cleft lip and palate |
| Q37 | - |  |  | SI | • Celiac disease |
| Q38 | - |  |  | SI | • Diabetes |
| Q39 | - |  |  | SI | • Gastroesophageal reflux |
| Q40 | - |  |  | SI | • Minor surgery |
| Q41 | - |  |  | SI | • Neuromuscular conditions |
| Q42 | - |  |  | SI | • Psychiatric disorders |
| Q43 | - |  |  | SI | • Respiratory Syncytial Virus (RSV) |
| Q44 | - |  |  | SI | • Single food allergy / intolerance |
| Q45 | - |  |  | SI | No nutritional implications |
| Q46 | - |  |  | SI | • Day case surgery |
| Q47 | - |  |  | SI | • Investigations |
| Q48 | - |  |  | SI | Guidelines for accurate measurement (step 3 above) |
| Q49 | - |  |  | SI | Tared weighing (infant or child will not lie or st... |
| Q50 | - |  |  | SI | 1. Weigh parent / carer barefoot and record in kg |
| Q51 | - |  |  | SI | 2. Weigh parent / carer and infant / child togethe... |
| Q52 | - |  |  | SI | 3. Subtract the parent / carer weight to obtain ch... |
| Q53 | - |  |  | SI | Infant (<2y) and child (≥2y) measuring requirement... |
| Q54 | - |  |  | SI | 1. Infant weighed unclothed |
| Q55 | - |  |  | SI | 2. Child weighed with minimal clothing |
| Q56 | - |  |  | SI | 3. Infant / child weight recorded to the nearest 0... |
| Q57 | - |  |  | SI | 4. Infant / child length / height recorded to near... |
| Q58 | - |  |  | SI | 5. Shoes and socks removed before length / height ... |
| Q59 | - |  |  | SI | 6. Child ≥ 2y that cannot stand: measure length an... |
| Q60 | - |  |  | SI | 7. Infant <2y that cannot lie down: measure standi... |
| Q61 | - |  |  | SI | Score |
| Q62 | - |  |  | SI | Classification |
| Q63 | - |  |  | SI | 0 - 1 |
| Q64 | - |  |  | SI | 2 - 3 |
| Q65 | - |  |  | SI | ≥ 4 |
| Q66 | - |  |  | SI | High risk |
| Q67 | - |  |  | SI | Medium risk |
| Q68 | - |  |  | SI | Low risk |
| Q69 | - |  |  | SI | The Screening Tool for the Assessment of Malnutrit... |
| Q70 | - |  |  | SI | and it designed for use with children in hospitals... |
| Q71 | - |  |  | SI | Date |
| Q72 | - |  |  | SI | Time os assessment |
| Q73 | - |  |  | SI | Time |
| Q74 | - |  |  | SI | Date |
| Q75 | - |  |  | SI | Time |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*