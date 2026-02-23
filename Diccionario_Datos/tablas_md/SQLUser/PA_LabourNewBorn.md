# SQLUser.PA_LabourNewBorn

**Schema:** SQLUser
**Columnas:** 41
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LNB_ALB_ParRef | varchar | PK |  | NO | PA_AdmLab Parent Reference |
| LNB_AbnormalDetails | varchar |  |  | SI | Abnormal Details |
| LNB_Abnormalities | varchar |  |  | SI | Abnormalities |
| LNB_ApgarScore1min | bigint |  |  | SI | Apgar Score after 1 min |
| LNB_ApgarScore5min | bigint |  |  | SI | Apgar Score after 5 min |
| LNB_BabyDischargedTo_DR | bigint |  | FK | SI | Des Ref Baby Discharged To |
| LNB_BirthOrderNumber | double |  |  | SI | Newborn No. |
| LNB_Birth_Weight | double |  |  | SI | Birth Weight |
| LNB_ChildSub | double |  |  | NO | ChildSub |
| LNB_CrownHeel | varchar |  |  | SI | Crown Heel |
| LNB_Defecation | varchar |  |  | SI | Defecation |
| LNB_DelivMethod_DR | bigint |  | FK | SI | Des REf DelivMethod |
| LNB_DeliveryDate | date |  |  | SI | Delivery Date |
| LNB_DischargeWeight | varchar |  |  | SI | Discharge Weight |
| LNB_FeedOnDischarge_DR | bigint |  | FK | SI | Des Ref Feed On Discharge |
| LNB_GradeDangCordNeck | double |  |  | SI | Grade of Danger of Cord Neck |
| LNB_Healthy | varchar |  |  | SI | Healthy Flag |
| LNB_Hpoglycaemia_DR | bigint |  | FK | SI | Des Ref Hpoglycaemia |
| LNB_ImmedCareReq_DR | bigint |  | FK | SI | Immed Care Req Des Ref to PacImmedCareReq |
| LNB_IntrauterineDeath | varchar |  |  | SI | Intrauterine Death |
| LNB_Jaundice_DR | bigint |  | FK | SI | Des Ref Jaundice |
| LNB_LowestGlucose | varchar |  |  | SI | Lowest Glucose |
| LNB_MaconiumStain_DR | bigint |  | FK | SI | Des Ref Maconium Stain |
| LNB_ManagementOfAbortion_DR | bigint |  | FK | SI | Des Ref ManagementOfAbortion |
| LNB_Maxbillrubin | varchar |  |  | SI | Max billrubin |
| LNB_OccipitoFrontalCircumference | varchar |  |  | SI | Occipito Frontal Circumference |
| LNB_OutcomeOfPregnancy_DR | bigint |  | FK | SI | Des Ref Outcome Of Pregnancy |
| LNB_PAADM_DR | bigint |  | FK | SI | Des Ref To PAADM |
| LNB_Phototherapy_DR | bigint |  | FK | SI | Des Ref Phototherapy |
| LNB_Present_DR | bigint |  | FK | SI | Des Ref Present |
| LNB_Respiration_DR | bigint |  | FK | SI | Respiration Des Ref to PacResp |
| LNB_RowID | varchar |  |  | NO | - |
| LNB_Sex_DR | bigint |  | FK | SI | Des Ref to CTSex |
| LNB_TimeApgar7 | varchar |  |  | SI | Time to reach Apgar7 |
| LNB_TimeOfBirth | time |  |  | SI | Time of Birth |
| LNB_TypeOfAbortion_DR | bigint |  | FK | SI | Des Ref TypeOfAbortion |
| LNB_Urination | varchar |  |  | SI | Urination |
| Q78Q1 | - |  |  | SI | Type of drink |
| Q78Q2 | - |  |  | SI | Amount |
| Q78Q3 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*