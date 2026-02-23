# SQLUser.OR_An_Oper_Additional_Staff

**Schema:** SQLUser
**Columnas:** 116
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OPAS_ParRef | varchar | PK |  | NO | OR_Anaest_Operation Parent Reference |
| OPAS_CPLocation_DR | bigint |  | FK | SI | Des Ref CT_Loc |
| OPAS_CareProvType | varchar |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017.2+ and re... |
| OPAS_CareProv_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| OPAS_Childsub | double |  |  | NO | Childsub |
| OPAS_EndDate | date |  |  | SI | End Date |
| OPAS_EndTime | time |  |  | SI | End Time |
| OPAS_NonCPAttendeeDetails | varchar |  |  | SI | Non CP Attendee Details |
| OPAS_OperatingStaffRole_DR | bigint |  | FK | SI | Des Ref ORC_OperatingStaffRole |
| OPAS_Operation_DR | bigint |  | FK | SI | Des Ref ORC_OPeration |
| OPAS_Remarks | varchar |  |  | SI | Remarks |
| OPAS_RowId | varchar |  |  | NO | - |
| OPAS_ShiftNumber | varchar |  |  | SI | Shift Number |
| OPAS_StartDate | date |  |  | SI | Start Date |
| OPAS_StartTime | time |  |  | SI | Start Time |
| OPAS_StatePPP_DR | bigint |  | FK | SI | des ref PAC_StatePPP |
| Q01 | - |  |  | SI | Dolor |
| Q02 | - |  |  | SI | Cansancio |
| Q03 | - |  |  | SI | Náuseas |
| Q04 | - |  |  | SI | Somnolencia |
| Q05 | - |  |  | SI | Depresión |
| Q06 | - |  |  | SI | Ansiedad |
| Q07 | - |  |  | SI | Apetito |
| Q08 | - |  |  | SI | Dificultad para respirar |
| Q09 | - |  |  | SI | Bienestar |
| Q10 | - |  |  | SI | Otro problema (por ejemplo, estreñimiento) |
| Q11 | - |  |  | SI | Descripción del problema |
| Q12 | - |  |  | SI | Gravedad del problema |
| Q13 | - |  |  | SI | Sin Dolor |
| Q14 | - |  |  | SI | El peor dolor posible |
| Q15 | - |  |  | SI | Sin cansancio |
| Q16 | - |  |  | SI | El peor cansancio posible |
| Q17 | - |  |  | SI | Sin náuseas |
| Q18 | - |  |  | SI | Las peores náuseas posibles |
| Q19 | - |  |  | SI | Sin somnolencia |
| Q20 | - |  |  | SI | La peor somnolencia posible |
| Q21 | - |  |  | SI | Sin depresión |
| Q22 | - |  |  | SI | La peor depresión posible |
| Q23 | - |  |  | SI | Sin ansiedad |
| Q24 | - |  |  | SI | La peor ansiedad posible |
| Q25 | - |  |  | SI | Sin apetito |
| Q26 | - |  |  | SI | El peor apetito posible |
| Q27 | - |  |  | SI | Sin dificultad para respirar |
| Q28 | - |  |  | SI | La peor dificultad para respirar posible |
| Q29 | - |  |  | SI | Mejor bienestar |
| Q30 | - |  |  | SI | El peor bienestar posible |
| Q31 | - |  |  | SI | Ningún problema |
| Q32 | - |  |  | SI | Lo peor posible |
| Q33 | - |  |  | SI | Un número más alto se asocia con una mayor graveda... |
| Q34 | - |  |  | SI | Cada puntuación representa la gravedad del síntoma... |
| Q35 | - |  |  | SI | El Sistema de Evaluación de Síntomas de Edmonton (... |
| Q36 | - |  |  | SI | 0 - 100: un número más alto se asocia con una mayo... |
| Q37 | - |  |  | SI | Dolor |
| Q38 | - |  |  | SI | Cansancio |
| Q39 | - |  |  | SI | Náuseas |
| Q40 | - |  |  | SI | Somnolencia |
| Q41 | - |  |  | SI | Depresión |
| Q42 | - |  |  | SI | Ansiedad |
| Q43 | - |  |  | SI | Apetito |
| Q44 | - |  |  | SI | Dificultad para respirar |
| Q45 | - |  |  | SI | Bienestar |
| Q46 | - |  |  | SI | Puntaje |
| Q47 | - |  |  | SI | Clasificación |
| Q48 | - |  |  | SI | 0 - 100 |
| Q49 | - |  |  | SI | Gravedad del problema |
| Q50 | - |  |  | SI | Dolor |
| Q51 | - |  |  | SI | Cansancio |
| Q52 | - |  |  | SI | Náuseas |
| Q53 | - |  |  | SI | Somnolencia |
| Q54 | - |  |  | SI | Depresión |
| Q55 | - |  |  | SI | Ansiedad |
| Q56 | - |  |  | SI | Apetito |
| Q57 | - |  |  | SI | Dificultad para respirar |
| Q58 | - |  |  | SI | Bienestar |
| Q59 | - |  |  | SI | Fecha |
| Q60 | - |  |  | SI | Hora |
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