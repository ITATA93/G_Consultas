# SQLUser.PA_ORAnOpAddStaffSnapshot

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAOAS_ParRef | bigint | PK |  | NO | PA_ORAnaestOper Parent Reference |
| PAOAS_CPLocation_DR | bigint |  | FK | SI | Des Ref CT_Loc |
| PAOAS_CareProvType | varchar |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017.2+ and re... |
| PAOAS_CareProv_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| PAOAS_Childsub | double |  |  | NO | Childsub |
| PAOAS_EndDate | date |  |  | SI | End Date |
| PAOAS_EndTime | time |  |  | SI | End Time |
| PAOAS_NonCPAttendeeDetails | varchar |  |  | SI | Non CP Attendee Details |
| PAOAS_OperatingStaffRole_DR | bigint |  | FK | SI | Des Ref ORC_OperatingStaffRole |
| PAOAS_Operation_DR | bigint |  | FK | SI | Des Ref ORC_OPeration |
| PAOAS_Remarks | varchar |  |  | SI | Remarks |
| PAOAS_RowId | varchar |  |  | NO | - |
| PAOAS_ShiftNumber | varchar |  |  | SI | Shift Number |
| PAOAS_StartDate | date |  |  | SI | Start Date |
| PAOAS_StartTime | time |  |  | SI | Start Time |
| PAOAS_StatePPP_DR | bigint |  | FK | SI | des ref PAC_StatePPP |
| Q01 | - |  |  | SI | AMBITO |
| Q02 | - |  |  | SI | PREGUNTAS PARA MEDIR RIESGOS |
| Q03 | - |  |  | SI | FACTOTES DE RIESGO |
| Q04 | - |  |  | SI | BAJO (Ausente) |
| Q05 | - |  |  | SI | ALTO (Presente) |
| Q06 | - |  |  | SI | ANAMNESIS |
| Q07 | - |  |  | SI | ¿La persona presenta situación de discapacidad y/o... |
| Q08 | - |  |  | SI | ¿La persona presenta una diabetes mellitus descomp... |
| Q09 | - |  |  | SI | CONDICIÓN CLÍNICA |
| Q10 | - |  |  | SI | ¿La persona presenta sangrado al sondeo en ma s de... |
| Q11 | - |  |  | SI | ¿La persona presenta mas de 8 sacos periodontales ... |
| Q12 | - |  |  | SI | Presencia de lesiones de caries activas que requie... |
| Q13 | - |  |  | SI | ¿Cuantas veces al día se cepilla los dientes la pe... |
| Q14 | - |  |  | SI | ¿La persona utiliza seda dental y/o cepillo interp... |
| Q15 | - |  |  | SI | ¿La persona se lava los dientes antes de ir a dorm... |
| Q16 | - |  |  | SI | HIGIENE |
| Q17 | - |  |  | SI | DIETA |
| Q18 | - |  |  | SI | ¿Cuantas veces al día la persona ingiere alimentos... |
| Q19 | - |  |  | SI | ¿La persona ingiere líquidos y/o alimentos azucara... |
| Q20 | - |  |  | SI | TABACO |
| Q21 | - |  |  | SI | ¿La persona fuma ma s de 10 cigarros al día? |
| Q22 | - |  |  | SI | FLUORURO |
| Q23 | - |  |  | SI | ¿Utiliza la persona pasta de dientes con 1000-1500... |
| Q24 | - |  |  | SI | MOTIVACIÓN |
| Q25 | - |  |  | SI | Luego de las preguntas anteriores, según usted (de... |
| Q26 | - |  |  | SI | ¿La persona tiene menos de 20 dientes en boca y no... |
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