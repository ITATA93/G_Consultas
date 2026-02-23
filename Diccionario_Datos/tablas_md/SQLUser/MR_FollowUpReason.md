# SQLUser.MR_FollowUpReason

**Schema:** SQLUser
**Columnas:** 175
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FUR_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| FUR_Childsub | double |  |  | NO | Childsub |
| FUR_FollowUpReason | varchar |  |  | SI | FollowUpReason |
| FUR_FollowUpReason_DR | bigint |  | FK | SI | Des Ref FollowUpReason |
| FUR_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Urinary frequency |
| Q01N | - |  |  | SI | Note |
| Q01ObsDR | - |  |  | SI | Urinary frequency DR |
| Q03 | - |  |  | SI | Nocturia |
| Q03N | - |  |  | SI | Note |
| Q03ObsDR | - |  |  | SI | Nocturia DR |
| Q04 | - |  |  | SI | Urine colour |
| Q04N | - |  |  | SI | Note |
| Q04ObsDR | - |  |  | SI | Urine colour DR |
| Q05 | - |  |  | SI | Haematuria |
| Q05N | - |  |  | SI | Note |
| Q05ObsDR | - |  |  | SI | Haematuria DR |
| Q07 | - |  |  | SI | Enuresis |
| Q07N | - |  |  | SI | Note |
| Q07ObsDR | - |  |  | SI | Enuresis DR |
| Q09 | - |  |  | SI | Dysuria (pain when urinating) |
| Q09N | - |  |  | SI | Note |
| Q09ObsDR | - |  |  | SI | Dysuria (pain when urinating) DR |
| Q11 | - |  |  | SI | Strangury |
| Q11N | - |  |  | SI | Note |
| Q11ObsDR | - |  |  | SI | Strangury DR |
| Q13 | - |  |  | SI | Renal replacement therapy |
| Q13N | - |  |  | SI | Note |
| Q13ObsDR | - |  |  | SI | Renal replacement therapy DR |
| Q15 | - |  |  | SI | Anuria |
| Q15N | - |  |  | SI | Note |
| Q15ObsDR | - |  |  | SI | Anuria DR |
| Q17 | - |  |  | SI | Oliguria |
| Q17N | - |  |  | SI | Note |
| Q17ObsDR | - |  |  | SI | Oliguria DR |
| Q21 | - |  |  | SI | Occasional incontinence (2 episodes per week) |
| Q21N | - |  |  | SI | Note |
| Q21ObsDR | - |  |  | SI | Occasional incontinence (2 episodes per week) DR |
| Q23 | - |  |  | SI | Urinary incontinence |
| Q23N | - |  |  | SI | Note |
| Q23ObsDR | - |  |  | SI | Urinary incontinence DR |
| Q25 | - |  |  | SI | Urinary catheter |
| Q25N | - |  |  | SI | Number |
| Q25ObsDR | - |  |  | SI | Urinary catheter DR |
| Q25P | - |  |  | SI | Positioned |
| Q25R | - |  |  | SI | Retention ml |
| Q25T | - |  |  | SI | Type |
| Q25TN | - |  |  | SI | Type |
| Q25TNObsDR | - |  |  | SI | Type DR |
| Q31 | - |  |  | SI | Condom catheter |
| Q31N | - |  |  | SI | Note |
| Q31ObsDR | - |  |  | SI | Condom catheter DR |
| Q33 | - |  |  | SI | Urinary stoma |
| Q33N | - |  |  | SI | Note |
| Q33ObsDR | - |  |  | SI | Urinary stoma DR |
| Q35 | - |  |  | SI | Nephrostomy left |
| Q35N | - |  |  | SI | Note |
| Q35ObsDR | - |  |  | SI | Nephrostomy left DR |
| Q36 | - |  |  | SI | Nephrostomy right |
| Q36N | - |  |  | SI | Note |
| Q36ObsDR | - |  |  | SI | Nephrostomy right DR |
| Q37 | - |  |  | SI | Cystostomy |
| Q37N | - |  |  | SI | Note |
| Q37ObsDR | - |  |  | SI | Cystostomy DR |
| Q39 | - |  |  | SI | Urinary incontinence pads |
| Q39N | - |  |  | SI | Note |
| Q39ObsDR | - |  |  | SI | Urinary incontinence pads DR |
| Q40 | - |  |  | SI | Intestinal |
| Q41 | - |  |  | SI | Melaena |
| Q41N | - |  |  | SI | Note |
| Q41ObsDR | - |  |  | SI | Melaena DR |
| Q43 | - |  |  | SI | Use of laxatives |
| Q43N | - |  |  | SI | Note |
| Q43ObsDR | - |  |  | SI | Use of laxatives DR |
| Q45 | - |  |  | SI | Diarrhoea |
| Q45N | - |  |  | SI | Note |
| Q45ObsDR | - |  |  | SI | Diarrhoea DR |
| Q47 | - |  |  | SI | Constipation |
| Q47N | - |  |  | SI | Note |
| Q47ObsDR | - |  |  | SI | Constipation DR |
| Q49 | - |  |  | SI | Incontinent bowel movements |
| Q49N | - |  |  | SI | Note |
| Q49ObsDR | - |  |  | SI | Incontinent bowel movements DR |
| Q51 | - |  |  | SI | Urinary incontinence pads |
| Q51N | - |  |  | SI | Note |
| Q51ObsDR | - |  |  | SI | Urinary incontinence pads DR |
| Q53 | - |  |  | SI | Stoma movements |
| Q53N | - |  |  | SI | Note |
| Q53ObsDR | - |  |  | SI | Stoma movements DR |
| Q55 | - |  |  | SI | Redness |
| Q55N | - |  |  | SI | Note |
| Q55ObsDR | - |  |  | SI | Redness DR |
| Q57 | - |  |  | SI | Intestinal injury |
| Q57N | - |  |  | SI | Note |
| Q57ObsDR | - |  |  | SI | Intestinal injury DR |
| Q59 | - |  |  | SI | Date and time of last bowel movement |
| Q60 | - |  |  | SI | Bowel movements check |
| Q60ObsDR | - |  |  | SI | Bowel movements check DR |
| Q62 | - |  |  | SI | Diuresis |
| Q63 | - |  |  | SI | Bristol stool scale |
| Q63N | - |  |  | SI | Note |
| Q63ObsDR | - |  |  | SI | Bristol stool scale DR |
| Q64 | - |  |  | SI | Bowel fluids (ml) |
| Q64N | - |  |  | SI | Note |
| Q64ObsDR | - |  |  | SI | Bowel fluids (ml) DR |
| Q65 | - |  |  | SI | Faecal colour |
| Q65N | - |  |  | SI | Note |
| Q65ObsDR | - |  |  | SI | Faecal colour DR |
| Q66 | - |  |  | SI | Incontinence bowel movements |
| Q66N | - |  |  | SI | Note |
| Q66ObsDR | - |  |  | SI | Incontinence bowel movements DR |
| Q73 | - |  |  | SI | Time of last bowel movement |
| Q74 | - |  |  | SI | Date |
| Q75 | - |  |  | SI | Time |
| Q76 | - |  |  | SI | Increased daytime urinary frequency |
| Q76ObsDR | - |  |  | SI | Increased daytime urinary frequency DR |
| Q77 | - |  |  | SI | Urinary voids per day |
| Q77ObsDR | - |  |  | SI | Urinary voids per day DR |
| Q78 | - |  |  | SI | Urinary Voids, Daytime |
| Q79 | - |  |  | SI | Note |
| Q80 | - |  |  | SI | Urinary Voids, Nighttime |
| Q81 | - |  |  | SI | Dietitian: |
| Q82 | - |  |  | SI | Consider referral if constipation or diarrhoea pre... |
| Q83 | - |  |  | SI | Continence Clinic: |
| Q84 | - |  |  | SI | Consider referral if occasional urinary  incontine... |
| Q85 | - |  |  | SI | Stomal Therapist: |
| Q86 | - |  |  | SI | Consider referral if incontinence of bowel movemen... |
| Q87 | - |  |  | SI | Referrals required |
| Q88 | - |  |  | SI | Other referrals required |
| Q89 | - |  |  | SI | This is an indication of referrals required. It do... |
| Q90 | - |  |  | SI | Note |
| Q91 | - |  |  | SI | Note |
| Q92 | - |  |  | SI | Catheter Size (Fr) |
| Q92ObsDR | - |  |  | SI | Catheter Size (Fr) DR |
| Q93 | - |  |  | SI | Date of next replacement |
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