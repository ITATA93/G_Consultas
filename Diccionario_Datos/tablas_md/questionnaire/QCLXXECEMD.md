# questionnaire.QCLXXECEMD

> Escala de Componentes de Evitación del Miedo al Dolor (FACS)

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala de Componentes de Evitación del Miedo al Dolor (FACS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | INSTRUCCIONES: La gente responde al dolor de difer... |
| Q02 | varchar |  |  | SI | En la última semana, ¿Cuánto está de acuerdo con l... |
| Q03 | varchar |  |  | SI | 1&nbsp; Trato de evitar actividades y movimientos ... |
| Q04 | varchar |  |  | SI | 2 &nbsp;Me preocupo por mi dolor |
| Q05 | varchar |  |  | SI | 3 &nbsp;Yo creo que mi dolor va a seguir empeorand... |
| Q06 | varchar |  |  | SI | 4 &nbsp;Me siento abrumado y con miedo cuando pien... |
| Q07 | varchar |  |  | SI | 5 &nbsp;Hay ciertas actividades que no intento por... |
| Q08 | varchar |  |  | SI | 6 &nbsp;Cuando mi dolor es realmente intenso, teng... |
| Q09 | varchar |  |  | SI | 7 &nbsp;Es injusto que yo tenga que vivir con mi d... |
| Q10 | varchar |  |  | SI | 8 &nbsp;Hay ciertas actividades y movimientos que ... |
| Q11 | varchar |  |  | SI | En la última semana, ¿Cuánto está de acuerdo con l... |
| Q12 | varchar |  |  | SI | 9 &nbsp;Debido a mi dolor, mi vida no es la misma |
| Q13 | varchar |  |  | SI | 10 No tengo ningún control sobre mi dolor |
| Q14 | varchar |  |  | SI | 11 Mi dolor me pone en riesgo de daños en el futur... |
| Q15 | varchar |  |  | SI | 12 Mi dolor es culpa de alguien más |
| Q16 | varchar |  |  | SI | 13 El dolor que siento es una señal de advertencia... |
| Q17 | varchar |  |  | SI | 14 Nadie entiende lo grave que es mi dolor |
| Q18 | varchar |  |  | SI | Termine cada una de las siguientes frases, empezan... |
| Q19 | varchar |  |  | SI | 15... actividades intensas (como trabajo pesado de... |
| Q20 | varchar |  |  | SI | 16... actividades moderadas (como cocinar o limpia... |
| Q21 | varchar |  |  | SI | 17... actividades ligeras (como ir al cine o salir... |
| Q22 | varchar |  |  | SI | 18... todas mis tareas en el hogar y/o en el traba... |
| Q23 | varchar |  |  | SI | 19... diversión y/o ejercicio (cosas que hago por ... |
| Q24 | varchar |  |  | SI | 20... actividades donde tengo que usar mi/s parte/... |
| Q25 | varchar |  |  | SI | En la última semana, debido a mi dolor, he evitado... |
| Q26 | date |  |  | SI | Fecha |
| Q27 | varchar |  |  | SI | Por favor, piensa sobre cómo ha estado en la últim... |
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