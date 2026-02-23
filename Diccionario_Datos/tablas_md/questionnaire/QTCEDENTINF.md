# questionnaire.QTCEDENTINF

**Schema:** questionnaire
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | Edad |
| Q02 | varchar | PK |  | SI | Alimentación |
| Q03 | varchar | PK |  | SI | Lactancia Materna Exclusiva |
| Q04 | varchar | PK |  | SI | N° de Mamaderas Nocturnas |
| Q05 | varchar | PK |  | SI | N° de Momentos de azúcar entre comidas |
| Q06 | varchar | PK |  | SI | Uso de medicamentos en jarabes azucarados |
| Q07 | varchar | PK |  | SI | Hábitos |
| Q08 | varchar | PK |  | SI | Higiene o hábito de cepillado |
| Q09 | varchar | PK |  | SI | Técnica de cepillado |
| Q10 | varchar | PK |  | SI | Chupete de entretención |
| Q11 | varchar | PK |  | SI | Succión digital |
| Q12 | varchar | PK |  | SI | Respuesta Bucal |
| Q13 | varchar | PK |  | SI | Examen de Salud Bucal |
| Q14 | varchar | PK |  | SI | Presencia de dientes supernumerarios |
| Q15 | varchar | PK |  | SI | Placa Bacteriana  |
| Q16 | numeric | PK |  | SI | N° de dientes con caries |
| Q17 | numeric | PK |  | SI | N° de dientes perdidos por caries |
| Q18 | numeric | PK |  | SI | N° de dientes obturados  |
| Q19 | varchar | PK |  | SI | Anormalidad Dentomaxilar |
| Q20 | varchar | PK |  | SI | Derivaciones |
| Q21 | bit | PK |  | SI | Por Riesgo |
| Q22 | bit | PK |  | SI | Por Daño |
| Q23 | varchar | PK |  | SI | Por Control Odontológico |
| QUESAnaDR | varchar | PK | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar | PK | FK | SI | Operation |
| QUESConsultDR | varchar | PK | FK | SI | Consult |
| QUESCopiedComments | varchar | PK |  | SI | Copied Comments |
| QUESCopiedDate | date | PK |  | SI | Copied Date |
| QUESCopiedEpDR | bigint | PK | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint | PK | FK | SI | Copied Source DR |
| QUESCopiedTime | time | PK |  | SI | Copied Time |
| QUESCopiedUserDR | bigint | PK | FK | SI | Copied User |
| QUESCreateDate | date | PK |  | SI | Creation Date |
| QUESCreateTime | time | PK |  | SI | Creation Time |
| QUESCreateUserDR | bigint | PK | FK | SI | Creation User |
| QUESDate | date | PK |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint | PK | FK | SI | Error Reason |
| QUESFHResidentDR | bigint | PK | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar | PK | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar | PK | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar | PK | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint | PK | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESPAPregnancyDR | bigint | PK | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint | PK | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar | PK | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar | PK | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar | PK | FK | SI | Appointment Outcome |
| QUESReasonForCorrectionDR | bigint | PK | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint | PK | FK | SI | Questionnaire |
| QUESScore | varchar | PK |  | SI | Score |
| QUESStatusDR | bigint | PK | FK | SI | Status |
| QUESTextResultDR | bigint | PK | FK | SI | Text Result |
| QUESTime | time | PK |  | SI | Last Update Time |
| QUESTransactionDR | varchar | PK | FK | SI | Transaction |
| QUESUserDR | bigint | PK | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*