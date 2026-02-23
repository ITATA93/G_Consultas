# questionnaire.QGXXXELI

> Elimination Diuresis and Intestinal

**Schema:** questionnaire
**Columnas:** 171
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Elimination Diuresis and Intestinal

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Urinary frequency |
| Q01N | varchar |  |  | SI | Note |
| Q01ObsDR | varchar |  | FK | SI | Urinary frequency DR |
| Q03 | varchar |  |  | SI | Nocturia |
| Q03N | varchar |  |  | SI | Note |
| Q03ObsDR | varchar |  | FK | SI | Nocturia DR |
| Q04 | varchar |  |  | SI | Urine colour |
| Q04N | varchar |  |  | SI | Note |
| Q04ObsDR | varchar |  | FK | SI | Urine colour DR |
| Q05 | varchar |  |  | SI | Haematuria |
| Q05N | varchar |  |  | SI | Note |
| Q05ObsDR | varchar |  | FK | SI | Haematuria DR |
| Q07 | varchar |  |  | SI | Enuresis |
| Q07N | varchar |  |  | SI | Note |
| Q07ObsDR | varchar |  | FK | SI | Enuresis DR |
| Q09 | varchar |  |  | SI | Dysuria (pain when urinating) |
| Q09N | varchar |  |  | SI | Note |
| Q09ObsDR | varchar |  | FK | SI | Dysuria (pain when urinating) DR |
| Q11 | varchar |  |  | SI | Strangury |
| Q11N | varchar |  |  | SI | Note |
| Q11ObsDR | varchar |  | FK | SI | Strangury DR |
| Q13 | varchar |  |  | SI | Renal replacement therapy |
| Q13N | varchar |  |  | SI | Note |
| Q13ObsDR | varchar |  | FK | SI | Renal replacement therapy DR |
| Q15 | varchar |  |  | SI | Anuria |
| Q15N | varchar |  |  | SI | Note |
| Q15ObsDR | varchar |  | FK | SI | Anuria DR |
| Q17 | varchar |  |  | SI | Oliguria |
| Q17N | varchar |  |  | SI | Note |
| Q17ObsDR | varchar |  | FK | SI | Oliguria DR |
| Q21 | varchar |  |  | SI | Occasional incontinence (2 episodes per week) |
| Q21N | varchar |  |  | SI | Note |
| Q21ObsDR | varchar |  | FK | SI | Occasional incontinence (2 episodes per week) DR |
| Q23 | varchar |  |  | SI | Urinary incontinence |
| Q23N | varchar |  |  | SI | Note |
| Q23ObsDR | varchar |  | FK | SI | Urinary incontinence DR |
| Q25 | varchar |  |  | SI | Urinary catheter |
| Q25N | varchar |  |  | SI | Number |
| Q25ObsDR | varchar |  | FK | SI | Urinary catheter DR |
| Q25P | varchar |  |  | SI | Positioned |
| Q25R | varchar |  |  | SI | Retention ml |
| Q25T | varchar |  |  | SI | Type |
| Q25TN | varchar |  |  | SI | Type |
| Q25TNObsDR | varchar |  | FK | SI | Type DR |
| Q31 | varchar |  |  | SI | Condom catheter |
| Q31N | varchar |  |  | SI | Note |
| Q31ObsDR | varchar |  | FK | SI | Condom catheter DR |
| Q33 | varchar |  |  | SI | Urinary stoma |
| Q33N | varchar |  |  | SI | Note |
| Q33ObsDR | varchar |  | FK | SI | Urinary stoma DR |
| Q35 | varchar |  |  | SI | Nephrostomy left |
| Q35N | varchar |  |  | SI | Note |
| Q35ObsDR | varchar |  | FK | SI | Nephrostomy left DR |
| Q36 | varchar |  |  | SI | Nephrostomy right |
| Q36N | varchar |  |  | SI | Note |
| Q36ObsDR | varchar |  | FK | SI | Nephrostomy right DR |
| Q37 | varchar |  |  | SI | Cystostomy |
| Q37N | varchar |  |  | SI | Note |
| Q37ObsDR | varchar |  | FK | SI | Cystostomy DR |
| Q39 | varchar |  |  | SI | Urinary incontinence pads |
| Q39N | varchar |  |  | SI | Note |
| Q39ObsDR | varchar |  | FK | SI | Urinary incontinence pads DR |
| Q40 | varchar |  |  | SI | Intestinal |
| Q41 | varchar |  |  | SI | Melaena |
| Q41N | varchar |  |  | SI | Note |
| Q41ObsDR | varchar |  | FK | SI | Melaena DR |
| Q43 | varchar |  |  | SI | Use of laxatives |
| Q43N | varchar |  |  | SI | Note |
| Q43ObsDR | varchar |  | FK | SI | Use of laxatives DR |
| Q45 | varchar |  |  | SI | Diarrhoea |
| Q45N | varchar |  |  | SI | Note |
| Q45ObsDR | varchar |  | FK | SI | Diarrhoea DR |
| Q47 | varchar |  |  | SI | Constipation |
| Q47N | varchar |  |  | SI | Note |
| Q47ObsDR | varchar |  | FK | SI | Constipation DR |
| Q49 | varchar |  |  | SI | Incontinent bowel movements |
| Q49N | varchar |  |  | SI | Note |
| Q49ObsDR | varchar |  | FK | SI | Incontinent bowel movements DR |
| Q51 | varchar |  |  | SI | Urinary incontinence pads |
| Q51N | varchar |  |  | SI | Note |
| Q51ObsDR | varchar |  | FK | SI | Urinary incontinence pads DR |
| Q53 | varchar |  |  | SI | Stoma movements |
| Q53N | varchar |  |  | SI | Note |
| Q53ObsDR | varchar |  | FK | SI | Stoma movements DR |
| Q55 | varchar |  |  | SI | Redness |
| Q55N | varchar |  |  | SI | Note |
| Q55ObsDR | varchar |  | FK | SI | Redness DR |
| Q57 | varchar |  |  | SI | Intestinal injury |
| Q57N | varchar |  |  | SI | Note |
| Q57ObsDR | varchar |  | FK | SI | Intestinal injury DR |
| Q59 | date |  |  | SI | Date and time of last bowel movement |
| Q60 | varchar |  |  | SI | Bowel movements check |
| Q60ObsDR | varchar |  | FK | SI | Bowel movements check DR |
| Q62 | varchar |  |  | SI | Diuresis |
| Q63 | varchar |  |  | SI | Bristol stool scale |
| Q63N | varchar |  |  | SI | Note |
| Q63ObsDR | varchar |  | FK | SI | Bristol stool scale DR |
| Q64 | varchar |  |  | SI | Bowel fluids (ml) |
| Q64N | varchar |  |  | SI | Note |
| Q64ObsDR | varchar |  | FK | SI | Bowel fluids (ml) DR |
| Q65 | varchar |  |  | SI | Faecal colour |
| Q65N | varchar |  |  | SI | Note |
| Q65ObsDR | varchar |  | FK | SI | Faecal colour DR |
| Q66 | varchar |  |  | SI | Incontinence bowel movements |
| Q66N | varchar |  |  | SI | Note |
| Q66ObsDR | varchar |  | FK | SI | Incontinence bowel movements DR |
| Q73 | time |  |  | SI | Time of last bowel movement |
| Q74 | date |  |  | SI | Date |
| Q75 | time |  |  | SI | Time |
| Q76 | varchar |  |  | SI | Increased daytime urinary frequency |
| Q76ObsDR | varchar |  | FK | SI | Increased daytime urinary frequency DR |
| Q77 | varchar |  |  | SI | Urinary voids per day |
| Q77ObsDR | varchar |  | FK | SI | Urinary voids per day DR |
| Q78 | numeric |  |  | SI | Urinary Voids, Daytime |
| Q79 | varchar |  |  | SI | Note |
| Q80 | numeric |  |  | SI | Urinary Voids, Nighttime |
| Q81 | varchar |  |  | SI | Dietitian: |
| Q82 | varchar |  |  | SI | Consider referral if constipation or diarrhoea pre... |
| Q83 | varchar |  |  | SI | Continence Clinic: |
| Q84 | varchar |  |  | SI | Consider referral if occasional urinary  incontine... |
| Q85 | varchar |  |  | SI | Stomal Therapist: |
| Q86 | varchar |  |  | SI | Consider referral if incontinence of bowel movemen... |
| Q87 | varchar |  |  | SI | Referrals required |
| Q88 | varchar |  |  | SI | Other referrals required |
| Q89 | varchar |  |  | SI | This is an indication of referrals required. It do... |
| Q90 | varchar |  |  | SI | Note |
| Q91 | varchar |  |  | SI | Note |
| Q92 | varchar |  |  | SI | Catheter Size (Fr) |
| Q92ObsDR | varchar |  | FK | SI | Catheter Size (Fr) DR |
| Q93 | date |  |  | SI | Date of next replacement |
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