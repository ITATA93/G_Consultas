# questionnaire.QTCEIECOG

> Informe Ecografía Ginecológica

**Schema:** questionnaire
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Informe Ecografía Ginecológica

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha de realización |
| Q02 | time |  |  | SI | Hora de realización |
| Q03 | varchar |  |  | SI | Indicación |
| Q04 | date |  |  | SI | FUR |
| Q05 | numeric |  |  | SI | Gestaciones |
| Q06 | numeric |  |  | SI | Partos |
| Q07 | varchar |  |  | SI | Transductor |
| Q08 | varchar |  |  | SI | Vejiga |
| Q09 | varchar |  |  | SI | Posición |
| Q10 | varchar |  |  | SI | Ubicación |
| Q11 | varchar |  |  | SI | Forma |
| Q12 | varchar |  |  | SI | Borde |
| Q13 | varchar |  |  | SI | Patrón Miometrial |
| Q14 | numeric |  |  | SI | Cuerpo Longitud (cms.) |
| Q15 | numeric |  |  | SI | Transverso (cms.) |
| Q16 | numeric |  |  | SI | Antero-Posterior (cms.) |
| Q17 | varchar |  |  | SI | Observaciones (útero) |
| Q18 | varchar |  |  | SI | Endometrio |
| Q19 | numeric |  |  | SI | Grosor (mms.) |
| Q20 | varchar |  |  | SI | Observaciones (Endometrio) |
| Q21 | varchar |  |  | SI | Fondo de saco de Douglas |
| Q22 | varchar |  |  | SI | Anexos |
| Q23 | numeric |  |  | SI | Longitud OD |
| Q24 | numeric |  |  | SI | Longitud OI |
| Q25 | numeric |  |  | SI | Transv. OD |
| Q26 | numeric |  |  | SI | Transv. OI |
| Q27 | numeric |  |  | SI | AP OD |
| Q28 | numeric |  |  | SI | AP OI |
| Q29 | numeric |  |  | SI | Volumen OD |
| Q30 | numeric |  |  | SI | Volumen OI |
| Q31 | varchar |  |  | SI | Otros Hallazgos |
| Q32 | varchar |  |  | SI | Observaciones Generales |
| Q33 | varchar |  |  | SI | Conclusión Ecográfica |
| Q34 | varchar |  |  | SI | Profesional que Realiza |
| Q35 | bigint |  |  | SI | Imagen |
| Q35TxtOnly | bigint |  |  | SI | Imagen Plain Text Only |
| Q36 | varchar |  |  | SI | Vejiga |
| Q37 | varchar |  |  | SI | Endometrio |
| Q38 | varchar |  |  | SI | Ovarios |
| Q39 | varchar |  |  | SI | Antecedentes Ginecológicos |
| Q40 | varchar |  |  | SI | Medidas |
| Q41 | varchar |  |  | SI | Vejiga |
| Q42 | varchar |  |  | SI | Fondo de Saco de Douglas |
| Q43 | varchar |  |  | SI | Utero |
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