# questionnaire.QTCCFBSPC

> Bariatric Surgery Preparation Checklist

**Schema:** questionnaire
**Columnas:** 110
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Bariatric Surgery Preparation Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Bariatric Surgery Preparation Checklist for: |
| Q02 | varchar |  |  | SI | To be checked for completion by the Bariatric surg... |
| Q03 | bit |  |  | SI | Morbidly obese (defined by WHO as a BMI > 40kg/m2 |
| Q04 | bit |  |  | SI | Comorbidities related to obesity that might be rem... |
| Q05 | bit |  |  | SI | Have attained a majority of skeletal muscle (great... |
| Q06 | bit |  |  | SI | Be at Tanner development stage 4 or greater |
| Q07 | bit |  |  | SI | Have a history of obesity for at least 3 years inc... |
| Q08 | bit |  |  | SI | All other attempts at behaviour modifications have... |
| Q09 | bit |  |  | SI | Express willingness to follow program requirements... |
| Q10 | varchar |  |  | SI | visits for a total of five years, and completing a... |
| Q11 | bit |  |  | SI | Agreed to avoid pregnancy for a year post-operativ... |
| Q12 | bit |  |  | SI | Not applicable |
| Q13 | bit |  |  | SI | Agreed to adhere to nutritional guidelines post-op... |
| Q14 | bit |  |  | SI | Has a supportive family environment |
| Q15 | bit |  |  | SI | Confirmation by a consultant/ specialist psychiatr... |
| Q16 | varchar |  |  | SI | implications of the surgery |
| Q17 | varchar |  |  | SI | To be checked for completion by the Bariatric surg... |
| Q18 | bit |  |  | SI | Physician/ Nurse license number checked against He... |
| Q19 | varchar |  |  | SI | Medical report/ Pre-operation assessment includes: |
| Q20 | bit |  |  | SI | Measure of height, weight and BMI |
| Q21 | bit |  |  | SI | Exclusion of primary cause for the obesity includi... |
| Q22 | bit |  |  | SI | Family history of cardiovascular disease (CVD) |
| Q23 | bit |  |  | SI | Family history of obesity |
| Q24 | bit |  |  | SI | Lipid profile |
| Q25 | bit |  |  | SI | Diabetes screen |
| Q26 | bit |  |  | SI | Fasting glucose and HBA1c |
| Q27 | bit |  |  | SI | Liver function tests |
| Q28 | bit |  |  | SI | Complete blood count |
| Q29 | bit |  |  | SI | Thyroid function tests screening for  micronutrien... |
| Q30 | bit |  |  | SI | Sleep study for patients with symptoms of obstruct... |
| Q31 | bit |  |  | SI | Bone age assessment considered for younger patient... |
| Q32 | bit |  |  | SI | Cardiac and pulmonary evaluation |
| Q33 | bit |  |  | SI | Endocrine evaluation |
| Q34 | bit |  |  | SI | Gastro oesophageal reflux disease |
| Q35 | bit |  |  | SI | Personal medical history |
| Q36 | bit |  |  | SI | Blood pressure |
| Q37 | bit |  |  | SI | Formal CVD risk score |
| Q38 | bit |  |  | SI | HBA1c ( if patient is diabetic) |
| Q39 | bit |  |  | SI | Waist hip ratio |
| Q40 | bit |  |  | SI | Sleep study ( if indicated) |
| Q41 | bit |  |  | SI | Not applicable |
| Q42 | bit |  |  | SI | Report from the consultant level bariatric surgeon... |
| Q43 | bit |  |  | SI | Report from a licensed dietician |
| Q44 | bit |  |  | SI | Report from paediatric consultant for psychologica... |
| Q45 | bit |  |  | SI | Report of support from psychiatrist |
| Q46 | bit |  |  | SI | Evidence of the delivery of a structured program f... |
| Q47 | bit |  |  | SI | Evidence of the delivery of a structured program f... |
| Q48 | varchar |  |  | SI | over 6 months; and six months of pharmacotherapy u... |
| Q49 | bit |  |  | SI | The signed consent form including evidence of risk... |
| Q50 | varchar |  |  | SI | INSTRUCTIONS FOR USE: |
| Q51 | varchar |  |  | SI | The Bariatric Surgery Preparation Checklist is dev... |
| Q52 | varchar |  |  | SI | The Bariatric Surgery Preparation Checklist should... |
| Q53 | varchar |  |  | SI | The Bariatric Surgeon should ensure that the check... |
| Q54 | varchar |  |  | SI | The Bariatric Surgery Preparation Checklist is to ... |
| Q55 | varchar |  |  | SI | May be used for handover and clinical reviews |
| Q56 | varchar |  |  | SI | REFERENCES: |
| Q57 | varchar |  |  | SI | Health Authority – Abu Dhabi (July 2013). HAAD sta... |
| Q58 | varchar |  |  | SI | BMI |
| Q59 | bit |  |  | SI | no comorbidities or |
| Q60 | bit |  |  | SI | morbidities |
| Q61 | bit |  |  | SI | evidence of failed non-invasive interventions, wei... |
| Q62 | bit |  |  | SI | morbidities |
| Q63 | bit |  |  | SI | evidence of failed non-invasive interventions, wei... |
| Q64 | bit |  |  | SI | at least 2 co-morbidities |
| Q65 | bit |  |  | SI | evidence of failed non-invasive interventions, wei... |
| Q66 | bit |  |  | SI | over a minimum period of six months and |
| Q67 | bit |  |  | SI | at least 3 co-morbidities |
| Q68 | varchar |  |  | SI | Eligibility criterion |
| Q69 | varchar |  |  | SI | Documentary evidence |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*