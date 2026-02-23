# SQLUser.MR_PsychDetails

**Schema:** SQLUser
**Columnas:** 147
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PSYCH_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| ChildQ01DR | - |  |  | SI | Child Reference: Items Count |
| PSYCH_Childsub | double |  |  | NO | Childsub |
| PSYCH_ConsentDate | date |  |  | SI | ConsentDate |
| PSYCH_ConsentDateTo | date |  |  | SI | ConsentDateTo |
| PSYCH_ConsentTime | time |  |  | SI | ConsentTime |
| PSYCH_DateFrom | date |  |  | SI | Date From |
| PSYCH_DateTo | date |  |  | SI | Date To |
| PSYCH_EmploymentStatus_DR | bigint |  | FK | SI | Des Ref EmploymentStatus |
| PSYCH_FirstAdmit | varchar |  |  | SI | First Admit |
| PSYCH_LegalStat_DR | bigint |  | FK | SI | Des Ref LegalStat |
| PSYCH_MentalCateg_DR | bigint |  | FK | SI | Des Ref MentalCateg |
| PSYCH_OnLeave | varchar |  |  | SI | OnLeave |
| PSYCH_PensionStatus_DR | bigint |  | FK | SI | Des Ref PensionStatus |
| PSYCH_PrevNonAdmit | varchar |  |  | SI | Prev Non Admit |
| PSYCH_RefFurtherCare_DR | bigint |  | FK | SI | Des Ref RefFurtherCare |
| PSYCH_RowId | varchar |  |  | NO | - |
| PSYCH_SectionDateFrom | date |  |  | SI | SectionDateFrom |
| PSYCH_SectionDateTo | date |  |  | SI | SectionDateTo |
| PSYCH_SectionTimeFrom | time |  |  | SI | SectionTimeFrom |
| PSYCH_SectionTimeTo | time |  |  | SI | SectionTimeTo |
| PSYCH_Status | varchar |  |  | SI | Status |
| PSYCH_TreatmentForm_DR | bigint |  | FK | SI | Des Ref TreatmentForm |
| PSYCH_UpdateDate | date |  |  | SI | UpdateDate |
| PSYCH_UpdateTime | time |  |  | SI | UpdateTime |
| PSYCH_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| PSYCH_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| PSYCH_UsualAccom_DR | bigint |  | FK | SI | Des Ref UsualAccom |
| Q01Q1 | - |  |  | SI | Item |
| Q01Q3 | - |  |  | SI | 1st Count |
| Q01Q4 | - |  |  | SI | 2nd Count |
| Q01Q5 | - |  |  | SI | 3rd Count |
| Q01Q6 | - |  |  | SI | Complete |
| Q01Q7 | - |  |  | SI | Incomplete |
| Q02 | - |  |  | SI | Resolution of Incomplete Count |
| Q03 | - |  |  | SI | Surgeon Informed |
| Q03Q2 | - |  |  | SI | Start |
| Q04 | - |  |  | SI | X-ray Performed |
| Q05 | - |  |  | SI | Incident Report Filed |
| Q06 | - |  |  | SI | Sponge And Instruments Resolved |
| Q07 | - |  |  | SI | Scrub Nurse: |
| Q08 | - |  |  | SI | Circulating Nurse: |
| Q09 | - |  |  | SI | Notes |
| Q10 | - |  |  | SI | Notes |
| Q11 | - |  |  | SI | Notes |
| Q12 | - |  |  | SI | Specify other: |
| Q20 | - |  |  | SI | Equipments |
| Q21 | - |  |  | SI | Scrub Nurse: |
| Q22 | - |  |  | SI | Circulating Nurse: |
| Q23 | - |  |  | SI | Type |
| Q24 | - |  |  | SI | Initial Count (Start) |
| Q25 | - |  |  | SI | Add |
| Q26 | - |  |  | SI | Final Count (Total) |
| Q27 | - |  |  | SI | Final Count (Expected) |
| Q28 | - |  |  | SI | Used |
| Q29 | - |  |  | SI | Raytec (2x2) |
| Q30 | - |  |  | SI | Raytec (2x2) Initial |
| Q31 | - |  |  | SI | Raytec (2x2) Add |
| Q32 | - |  |  | SI | Raytec (2x2) Expected |
| Q33 | - |  |  | SI | Raytec 2x2 Final Count |
| Q34 | - |  |  | SI | Raytec (4x4) |
| Q35 | - |  |  | SI | Raytec (4x4) I |
| Q36 | - |  |  | SI | Raytec (4x4) A |
| Q37 | - |  |  | SI | Raytec (4x4) F.E. |
| Q38 | - |  |  | SI | Raytec (4x4) F C |
| Q39 | - |  |  | SI | Gauze pad long |
| Q40 | - |  |  | SI | Gauze pad long I |
| Q41 | - |  |  | SI | Gauze pad long A |
| Q42 | - |  |  | SI | Gauze pad long F E |
| Q43 | - |  |  | SI | Gauze pad long F C |
| Q44 | - |  |  | SI | Roll swab |
| Q45 | - |  |  | SI | Roll swab I |
| Q46 | - |  |  | SI | Roll swab A |
| Q47 | - |  |  | SI | Roll swab F E |
| Q48 | - |  |  | SI | Roll F C |
| Q49 | - |  |  | SI | ABD swab |
| Q50 | - |  |  | SI | ABD swab I |
| Q51 | - |  |  | SI | ABD swab A |
| Q52 | - |  |  | SI | ABD swab F E |
| Q53 | - |  |  | SI | ABD Swab F C |
| Q54 | - |  |  | SI | Peanut |
| Q55 | - |  |  | SI | Peanut I |
| Q56 | - |  |  | SI | Peanut A |
| Q57 | - |  |  | SI | Peanut F E |
| Q58 | - |  |  | SI | Peanut F C |
| Q59 | - |  |  | SI | Cottonoid |
| Q60 | - |  |  | SI | Cottonoid I |
| Q61 | - |  |  | SI | Cottonoid A |
| Q62 | - |  |  | SI | Cottonoid F E |
| Q63 | - |  |  | SI | Cottonoid F C |
| Q64 | - |  |  | SI | Blades |
| Q65 | - |  |  | SI | Blades F C |
| Q66 | - |  |  | SI | Blades I |
| Q67 | - |  |  | SI | Blades A |
| Q68 | - |  |  | SI | Blades F E |
| Q69 | - |  |  | SI | Needle |
| Q70 | - |  |  | SI | Needle I |
| Q71 | - |  |  | SI | Needle A |
| Q72 | - |  |  | SI | Needle F E |
| Q73 | - |  |  | SI | Needle F C |
| Q74 | - |  |  | SI | Guide wire / Misc. Items |
| Q75 | - |  |  | SI | Guide wire / Misc. Items I |
| Q76 | - |  |  | SI | Guide wire / Misc. Items A |
| Q77 | - |  |  | SI | Guide wire / Misc. Items F E |
| Q78 | - |  |  | SI | Guide wire / Misc. Items F C |
| Q79 | - |  |  | SI | Date |
| Q80 | - |  |  | SI | Time |
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