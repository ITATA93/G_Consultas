# SQLUser.ARC_PayAgreemBedDiscount

**Schema:** SQLUser
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BD_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| BD_Childsub | double |  |  | NO | Childsub |
| BD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BD_CreatedDate | date |  |  | SI | Created Date |
| BD_CreatedTime | time |  |  | SI | Created Time |
| BD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BD_DateFrom | date |  |  | SI | Date From |
| BD_DateTo | date |  |  | SI | Date To |
| BD_DayFrom | double |  |  | SI | Day From |
| BD_DayTo | double |  |  | SI | Day To |
| BD_Discount | double |  |  | SI | % Discount |
| BD_RoomType_DR | bigint |  | FK | SI | Des Ref RoomType |
| BD_RowId | varchar |  |  | NO | - |
| BD_UpdatedDate | date |  |  | SI | Updated Date |
| BD_UpdatedTime | time |  |  | SI | Updated Time |
| BD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | INSTRUCCIONES: La gente responde al dolor de difer... |
| Q02 | - |  |  | SI | En la última semana, ¿Cuánto está de acuerdo con l... |
| Q03 | - |  |  | SI | 1&nbsp |
| Q04 | - |  |  | SI | 2 &nbsp |
| Q05 | - |  |  | SI | 3 &nbsp |
| Q06 | - |  |  | SI | 4 &nbsp |
| Q07 | - |  |  | SI | 5 &nbsp |
| Q08 | - |  |  | SI | 6 &nbsp |
| Q09 | - |  |  | SI | 7 &nbsp |
| Q10 | - |  |  | SI | 8 &nbsp |
| Q11 | - |  |  | SI | En la última semana, ¿Cuánto está de acuerdo con l... |
| Q12 | - |  |  | SI | 9 &nbsp |
| Q13 | - |  |  | SI | 10 No tengo ningún control sobre mi dolor |
| Q14 | - |  |  | SI | 11 Mi dolor me pone en riesgo de daños en el futur... |
| Q15 | - |  |  | SI | 12 Mi dolor es culpa de alguien más |
| Q16 | - |  |  | SI | 13 El dolor que siento es una señal de advertencia... |
| Q17 | - |  |  | SI | 14 Nadie entiende lo grave que es mi dolor |
| Q18 | - |  |  | SI | Termine cada una de las siguientes frases, empezan... |
| Q19 | - |  |  | SI | 15... actividades intensas (como trabajo pesado de... |
| Q20 | - |  |  | SI | 16... actividades moderadas (como cocinar o limpia... |
| Q21 | - |  |  | SI | 17... actividades ligeras (como ir al cine o salir... |
| Q22 | - |  |  | SI | 18... todas mis tareas en el hogar y/o en el traba... |
| Q23 | - |  |  | SI | 19... diversión y/o ejercicio (cosas que hago por ... |
| Q24 | - |  |  | SI | 20... actividades donde tengo que usar mi/s parte/... |
| Q25 | - |  |  | SI | En la última semana, debido a mi dolor, he evitado... |
| Q26 | - |  |  | SI | Fecha |
| Q27 | - |  |  | SI | Por favor, piensa sobre cómo ha estado en la últim... |
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