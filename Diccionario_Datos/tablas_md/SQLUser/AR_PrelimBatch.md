# SQLUser.AR_PrelimBatch

**Schema:** SQLUser
**Columnas:** 135
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PBAT_RowId | bigint | PK |  | NO | - |
| PBAT_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| PBAT_BillDateFrom | date |  |  | SI | Bill Date From |
| PBAT_BillDateTo | date |  |  | SI | Bill Date To |
| PBAT_BillDesc_DR | bigint |  | FK | SI | Des Ref ARCBillDescription |
| PBAT_DateCreated | date |  |  | SI | Date Created |
| PBAT_DatePrinted | date |  |  | SI | Date Printed |
| PBAT_EpisodeType | varchar |  |  | SI | Episode Type |
| PBAT_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| PBAT_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| PBAT_InvoiceNumber | varchar |  |  | SI | Invoice Number |
| PBAT_Number | varchar |  |  | SI | Batch Number |
| PBAT_PostOfficeRefNumber | varchar |  |  | SI | Post Office Reference Number |
| PBAT_PrelimBatchStatus | varchar |  |  | SI | PrelimBatchStatus |
| PBAT_ProgressStatus_DR | bigint |  | FK | SI | Des Ref ARCBillProgressStatus |
| PBAT_SubmissionID | varchar |  |  | SI | Submission ID |
| PBAT_TimeCreated | time |  |  | SI | Time Created |
| PBAT_TimePrinted | time |  |  | SI | Time Printed |
| PBAT_UserCreated_DR | bigint |  | FK | SI | Des Ref User |
| PBAT_UserPrinted_DR | bigint |  | FK | SI | Des Ref UserPrinted |
| PBAT_XMLFileName | varchar |  |  | SI | XML File Name |
| Q01 | - |  |  | SI | 1. Que día de la semana es hoy |
| Q02 | - |  |  | SI | Ahora me gustaría hacerle una preguntas para ver c... |
| Q03 | - |  |  | SI | 2. Cual es la fecha de hoy |
| Q04 | - |  |  | SI | Respuesta 1 |
| Q05 | - |  |  | SI | respuesta 2 |
| Q06 | - |  |  | SI | 3. En qué mes estamos |
| Q07 | - |  |  | SI | 4. En qué estación del año estamos |
| Q08 | - |  |  | SI | respuesta 3 |
| Q09 | - |  |  | SI | respuesta 4 |
| Q10 | - |  |  | SI | 5. En qué año estamos |
| Q11 | - |  |  | SI | respuesta 5 |
| Q12 | - |  |  | SI | 6. Qué dirección es esta (calle, número) |
| Q13 | - |  |  | SI | respuesta 6 |
| Q14 | - |  |  | SI | 7. En qué país estamos |
| Q15 | - |  |  | SI | respuesta 7 |
| Q16 | - |  |  | SI | 8. En qué ciudad estamos |
| Q17 | - |  |  | SI | respuesta 8 |
| Q18 | - |  |  | SI | 9. Cuáles son las dos calles principales cerca de ... |
| Q19 | - |  |  | SI | respuesta 9 |
| Q20 | - |  |  | SI | 10. En qué piso estamos |
| Q21 | - |  |  | SI | 11. Árbol |
| Q22 | - |  |  | SI | respuesta 11 |
| Q23 | - |  |  | SI | 12. Mesa |
| Q24 | - |  |  | SI | respuesta 12 |
| Q25 | - |  |  | SI | 13. Avión |
| Q26 | - |  |  | SI | respuesta 13 |
| Q27 | - |  |  | SI | NÚMERO DE RESPUESTAS CORRECTAS |
| Q28 | - |  |  | SI | NÚMERO DE REPETICIONES |
| Q29 | - |  |  | SI | 14.a 93 |
| Q30 | - |  |  | SI | respuesta 14 |
| Q31 | - |  |  | SI | 15.a 86 |
| Q32 | - |  |  | SI | respuesta 15 |
| Q33 | - |  |  | SI | 16.a 79 |
| Q34 | - |  |  | SI | respuesta 16 |
| Q35 | - |  |  | SI | 17.a 72 |
| Q36 | - |  |  | SI | respuesta 17 |
| Q37 | - |  |  | SI | 18.a 65 |
| Q38 | - |  |  | SI | respuesta 18 |
| Q39 | - |  |  | SI | 14.b 9 |
| Q40 | - |  |  | SI | respuesta 14 b |
| Q41 | - |  |  | SI | 15.b 7 |
| Q42 | - |  |  | SI | respuesta 15 b |
| Q43 | - |  |  | SI | 16.b 5 |
| Q44 | - |  |  | SI | respuesta 16 b |
| Q45 | - |  |  | SI | 17.b 3 |
| Q46 | - |  |  | SI | respuesta 17 b |
| Q47 | - |  |  | SI | 18.b 1 |
| Q48 | - |  |  | SI | respuesta 18 b |
| Q49 | - |  |  | SI | 19. Árbol |
| Q50 | - |  |  | SI | respuesta 19 |
| Q51 | - |  |  | SI | 20. Mesa |
| Q52 | - |  |  | SI | respuesta 20 |
| Q53 | - |  |  | SI | 21. Avión |
| Q54 | - |  |  | SI | respuesta 21 |
| Q55 | - |  |  | SI | 22. ¿Qué es esto? |
| Q56 | - |  |  | SI | respuesta 22 |
| Q57 | - |  |  | SI | 23. ¿Cómo se llama esto? |
| Q58 | - |  |  | SI | respuesta 23 |
| Q59 | - |  |  | SI | 24. |
| Q60 | - |  |  | SI | respuesta 24 |
| Q61 | - |  |  | SI | 25.a |
| Q62 | - |  |  | SI | respuesta 25a |
| Q63 | - |  |  | SI | 25.b |
| Q64 | - |  |  | SI | respuesta 25b |
| Q65 | - |  |  | SI | 26 |
| Q66 | - |  |  | SI | respuesta 26 |
| Q67 | - |  |  | SI | 27 |
| Q68 | - |  |  | SI | respuesta 27 |
| Q69 | - |  |  | SI | 28.a Pentágonos (incorrecto:0 |
| Q70 | - |  |  | SI | respuesta 28a |
| Q71 | - |  |  | SI | 29.b Círculos  (incorrecto:0 |
| Q72 | - |  |  | SI | respuest 28 b |
| Q73 | - |  |  | SI | respuesta 10 |
| Q74 | - |  |  | SI | Resultado: |
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