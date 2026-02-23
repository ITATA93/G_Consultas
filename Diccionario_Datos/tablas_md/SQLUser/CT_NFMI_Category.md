# SQLUser.CT_NFMI_Category

**Schema:** SQLUser
**Columnas:** 189
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NFMI_RowId | bigint | PK |  | NO | - |
| NFMI_Code | varchar |  |  | NO | Code |
| NFMI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| NFMI_CreatedDate | date |  |  | SI | Created Date |
| NFMI_CreatedTime | time |  |  | SI | Created Time |
| NFMI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NFMI_DateFrom | date |  |  | SI | DateFrom |
| NFMI_DateTo | date |  |  | SI | DateTo |
| NFMI_Desc | varchar |  |  | NO | Description |
| NFMI_GovSubCateg_DR | varchar |  | FK | SI | Des REf SubGovCateg |
| NFMI_InsBatchOnly | varchar |  |  | SI | Insur Batch Only |
| NFMI_LinkNFMI_DR | bigint |  | FK | SI | Des Ref NFMI |
| NFMI_Owner | varchar |  |  | SI | Owner |
| NFMI_UpdatedDate | date |  |  | SI | Updated Date |
| NFMI_UpdatedTime | time |  |  | SI | Updated Time |
| NFMI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Introduction |
| Q02 | - |  |  | SI | Introduction (Please read to consumer) |
| Q03 | - |  |  | SI | Thank you for agreeing to take part in this brief ... |
| Q04 | - |  |  | SI | and in the past three months. These substances can... |
| Q05 | - |  |  | SI | sedatives, pain medications). For this interview, ... |
| Q06 | - |  |  | SI | more frequently or at higher doses than prescribed... |
| Q07 | - |  |  | SI | strictly confidential. |
| Q08 | - |  |  | SI | Q1. In your life which of the following substances... |
| Q09 | - |  |  | SI | Probe if answers are all negative: Not even when y... |
| Q10 | - |  |  | SI | No, to all items, stop interview. |
| Q100 | - |  |  | SI | Amphetamine Type Stimulants Score |
| Q101 | - |  |  | SI | Inhalants Score |
| Q102 | - |  |  | SI | Sedatives Score |
| Q103 | - |  |  | SI | Hallucinogens Score |
| Q104 | - |  |  | SI | Opioids Score |
| Q105 | - |  |  | SI | Other Score |
| Q106 | - |  |  | SI | Alcohol Score |
| Q107 | - |  |  | SI | Tobacco Score |
| Q108 | - |  |  | SI | Cannabis Score |
| Q109 | - |  |  | SI | Cocaine Score |
| Q11 | - |  |  | SI | Q2. In the past three months, how often have you u... |
| Q110 | - |  |  | SI | Amphetamine Type Stimulants Score |
| Q111 | - |  |  | SI | Inhalants Score |
| Q112 | - |  |  | SI | Sedatives Score |
| Q113 | - |  |  | SI | Hallucinogens Score |
| Q114 | - |  |  | SI | Opioids Score |
| Q115 | - |  |  | SI | Other Score |
| Q116 | - |  |  | SI | The ASSIST is a brief screening questionnaire to f... |
| Q117 | - |  |  | SI | Low. No treatment required. No Referral |
| Q118 | - |  |  | SI | Moderate. Further assessment, consultation with al... |
| Q119 | - |  |  | SI | High. Further assessment, consultation with alcoho... |
| Q12 | - |  |  | SI | a) Tobacco (Cigarettes, chewing tobacco, cigars) |
| Q120 | - |  |  | SI | dependent use of alcohol, tobacco and other psycho... |
| Q121 | - |  |  | SI | Please read the instructions to the customer |
| Q122 | - |  |  | SI | Date |
| Q123 | - |  |  | SI | Time |
| Q124 | - |  |  | SI | Tobacco Score |
| Q125 | - |  |  | SI | Alcohol Score |
| Q126 | - |  |  | SI | Cannabis Score |
| Q127 | - |  |  | SI | Cocaine Score |
| Q128 | - |  |  | SI | Amphetamine Type Stimulants Score |
| Q129 | - |  |  | SI | Inhalants Score |
| Q13 | - |  |  | SI | b) Alcohol (Beer, wine, sprits) |
| Q130 | - |  |  | SI | Sedatives Score |
| Q131 | - |  |  | SI | Hallucinogens Score |
| Q132 | - |  |  | SI | Opioids Score |
| Q133 | - |  |  | SI | Other Score |
| Q14 | - |  |  | SI | c) Cannabis (Marijuana, pot, grass, hash) |
| Q15 | - |  |  | SI | d) Cocaine (Coke, crack) |
| Q16 | - |  |  | SI | e) Amphetamine Type Stimulants (Speed, meth, ice, ... |
| Q17 | - |  |  | SI | f) Inhalants (Nitrous, glue, petrol, paint thinner... |
| Q18 | - |  |  | SI | g) Sedatives (Valium, Serepax, Rohypnol) |
| Q19 | - |  |  | SI | h) Hallucinogens (Lysergic acid diethylamide (LSD)... |
| Q20 | - |  |  | SI | i) Opioids (Heroin, morphine, methadone, codeine) |
| Q21 | - |  |  | SI | j) Other. Kava, Gamma-hydroxybutyrate (GHB), exces... |
| Q22 | - |  |  | SI | Note: If answered: never for a substance in the la... |
| Q23 | - |  |  | SI | Q3. During the past 3 months, how often have you h... |
| Q24 | - |  |  | SI | a) Tobacco (Cigarettes, chewing tobacco, cigars) |
| Q25 | - |  |  | SI | b) Alcohol (Beer, wine, sprits) |
| Q26 | - |  |  | SI | c) Cannabis (Marijuana, pot, grass, hash) |
| Q27 | - |  |  | SI | d) Cocaine (Coke, crack) |
| Q28 | - |  |  | SI | e) Amphetamine Type Stimulants (Speed, meth, ice, ... |
| Q29 | - |  |  | SI | f) Inhalants (Nitrous, glue, petrol, paint thinner... |
| Q30 | - |  |  | SI | g) Sedatives (Valium, Serepax, Rohypnol) |
| Q31 | - |  |  | SI | h) Hallucinogens (Lysergic acid diethylamide (LSD)... |
| Q32 | - |  |  | SI | i) Opioids (Heroin, morphine, methadone, codeine) |
| Q33 | - |  |  | SI | j) Other. Kava, Gamma-hydroxybutyrate (GHB), exces... |
| Q34 | - |  |  | SI | Q4. During the past three months how often has you... |
| Q35 | - |  |  | SI | a) Tobacco (Cigarettes, chewing tobacco, cigars) |
| Q36 | - |  |  | SI | b) Alcohol (Beer, wine, sprits) |
| Q37 | - |  |  | SI | c) Cannabis (Marijuana, pot, grass, hash) |
| Q38 | - |  |  | SI | d) Cocaine (Coke, crack) |
| Q39 | - |  |  | SI | e) Amphetamine Type Stimulants (Speed, meth, ice, ... |
| Q40 | - |  |  | SI | f) Inhalants (Nitrous, glue, petrol, paint thinner... |
| Q41 | - |  |  | SI | g) Sedatives (Valium, Serepax, Rohypnol) |
| Q42 | - |  |  | SI | h) Hallucinogens (Lysergic acid diethylamide (LSD)... |
| Q43 | - |  |  | SI | i) Opioids (Heroin, morphine, methadone, codeine) |
| Q44 | - |  |  | SI | j) Other. Kava, Gamma-hydroxybutyrate (GHB), exces... |
| Q45 | - |  |  | SI | Prompt consumer with examples of possible problems |
| Q46 | - |  |  | SI | Q5. During the past 3 months how often have you fa... |
| Q47 | - |  |  | SI | a) Tobacco (Cigarettes, chewing tobacco, cigars) |
| Q48 | - |  |  | SI | b) Alcohol (Beer, wine, sprits) |
| Q49 | - |  |  | SI | c) Cannabis (Marijuana, pot, grass, hash) |
| Q50 | - |  |  | SI | d) Cocaine (Coke, crack) |
| Q51 | - |  |  | SI | e) Amphetamine Type Stimulants (Speed, meth, ice, ... |
| Q52 | - |  |  | SI | f) Inhalants (Nitrous, glue, petrol, paint thinner... |
| Q53 | - |  |  | SI | g) Sedatives (Valium, Serepax, Rohypnol) |
| Q54 | - |  |  | SI | h) Hallucinogens (Lysergic acid diethylamide (LSD)... |
| Q55 | - |  |  | SI | i) Opioids (Heroin, morphine, methadone, codeine) |
| Q56 | - |  |  | SI | j) Other. Kava, Gamma-hydroxybutyrate (GHB), exces... |
| Q57 | - |  |  | SI | Ask Questions 6 & 7 for all substances used in lif... |
| Q58 | - |  |  | SI | Q7. Have you ever tried and failed to control, cut... |
| Q59 | - |  |  | SI | a) Tobacco (Cigarettes, chewing tobacco, cigars) |
| Q60 | - |  |  | SI | b) Alcohol (Beer, wine, sprits) |
| Q61 | - |  |  | SI | c) Cannabis (Marijuana, pot, grass, hash) |
| Q62 | - |  |  | SI | d) Cocaine (Coke, crack) |
| Q63 | - |  |  | SI | e) Amphetamine Type Stimulants (Speed, meth, ice, ... |
| Q64 | - |  |  | SI | f) Inhalants (Nitrous, glue, petrol, paint thinner... |
| Q65 | - |  |  | SI | g) Sedatives (Valium, Serepax, Rohypnol) |
| Q66 | - |  |  | SI | h) Hallucinogens (Lysergic acid diethylamide (LSD)... |
| Q67 | - |  |  | SI | i) Opioids (Heroin, morphine, methadone, codeine) |
| Q68 | - |  |  | SI | j) Other. Kava, Gamma-hydroxybutyrate (GHB), exces... |
| Q69 | - |  |  | SI | Q8. Have you ever used any drug by injection (non-... |
| Q70 | - |  |  | SI | Used in past 3 months and pattern of injecting: |
| Q71 | - |  |  | SI | Provide Brief Intervention plus ‘Injecting Risks’ ... |
| Q72 | - |  |  | SI | Further assessment & more intensive treatment |
| Q73 | - |  |  | SI | Q6. Has a friend or relative or anyone else ever e... |
| Q74 | - |  |  | SI | a) Tobacco (Cigarettes, chewing tobacco, cigars) |
| Q75 | - |  |  | SI | b) Alcohol (Beer, wine, sprits) |
| Q76 | - |  |  | SI | c) Cannabis (Marijuana, pot, grass, hash) |
| Q77 | - |  |  | SI | d) Cocaine (Coke, crack) |
| Q78 | - |  |  | SI | e) Amphetamine Type Stimulants (Speed, meth, ice, ... |
| Q79 | - |  |  | SI | f) Inhalants (Nitrous, glue, petrol, paint thinner... |
| Q80 | - |  |  | SI | g) Sedatives (Valium, Serepax, Rohypnol) |
| Q81 | - |  |  | SI | h) Hallucinogens (Lysergic acid diethylamide (LSD)... |
| Q82 | - |  |  | SI | i) Opioids (Heroin, morphine, methadone, codeine) |
| Q83 | - |  |  | SI | j) Other. Kava, Gamma-hydroxybutyrate (GHB), exces... |
| Q84 | - |  |  | SI | Risk |
| Q85 | - |  |  | SI | Treatment |
| Q86 | - |  |  | SI | Referral |
| Q87 | - |  |  | SI | Low (Drugs 0-3, alcohol 0-10) |
| Q88 | - |  |  | SI | Moderate (Drugs 4-26, Alcohol 11-26) |
| Q89 | - |  |  | SI | High (27 or above) |
| Q90 | - |  |  | SI | None required |
| Q91 | - |  |  | SI | Further assessment, consultation with alcohol and ... |
| Q92 | - |  |  | SI | Further assessment, consultation with alcohol and ... |
| Q93 | - |  |  | SI | No referral |
| Q94 | - |  |  | SI | Referral |
| Q95 | - |  |  | SI | Urgent referral |
| Q96 | - |  |  | SI | Alcohol Score |
| Q97 | - |  |  | SI | Tobacco Score |
| Q98 | - |  |  | SI | Cannabis Score |
| Q99 | - |  |  | SI | Cocaine Score |
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