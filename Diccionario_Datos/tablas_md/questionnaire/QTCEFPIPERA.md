# questionnaire.QTCEFPIPERA

**Schema:** questionnaire
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| QC1F1 | varchar | PK |  | SI | Tabaquismo |
| QC1F10 | varchar | PK |  | SI | Hist. Disnea Recurrentes |
| QC1F11 | varchar | PK |  | SI | Alivio |
| QC1F12 | varchar | PK |  | SI | O.B. relacionadas con |
| QC1F13 | varchar | PK |  | SI | Recurrencia |
| QC1F14 | varchar | PK |  | SI | Antecedentes Personales |
| QC1F15 | varchar | PK |  | SI | Antecedentes Familiares |
| QC1F16 | varchar | PK |  | SI | Patologias cronicas |
| QC1F17 | varchar | PK |  | SI | Observaciones |
| QC1F18 | varchar | PK |  | SI | Medicamentos |
| QC1F19 | varchar | PK |  | SI | Tos |
| QC1F2 | varchar | PK |  | SI | Ex Fumador |
| QC1F20 | varchar | PK |  | SI | Observaciones EFP |
| QC1F21 | varchar | PK |  | SI | Rx de Torax |
| QC1F22 | varchar | PK |  | SI | Baciloscopia |
| QC1F23 | varchar | PK |  | SI | PEF Teorico |
| QC1F24 | varchar | PK |  | SI | PEF Obtenido |
| QC1F25 | varchar | PK |  | SI | PEF Post B2 |
| QC1F26 | varchar | PK |  | SI | Espirometria |
| QC1F27 | varchar | PK |  | SI | Hemograma |
| QC1F28 | varchar | PK |  | SI | Uremia |
| QC1F29 | varchar | PK |  | SI | Glicemia |
| QC1F3 | varchar | PK |  | SI | Fumador Pasivo |
| QC1F30 | varchar | PK |  | SI | Orina |
| QC1F31 | varchar | PK |  | SI | Sedimentacion |
| QC1F32 | varchar | PK |  | SI | Diagnostico |
| QC1F33 | varchar | PK |  | SI | Observaciones Examenes |
| QC1F34 | varchar | PK |  | SI | Tratamiento |
| QC1F35 | varchar | PK |  | SI | Anamnesis |
| QC1F36 | varchar | PK |  | SI | Frecuencia Respiratoria |
| QC1F37 | varchar | PK |  | SI | Frecuencia Cardiaca |
| QC1F38 | varchar | PK |  | SI | Presion Arterial |
| QC1F39 | varchar | PK |  | SI | Llenado Capilar |
| QC1F4 | varchar | PK |  | SI | Exposicion a Contaminantes |
| QC1F40 | varchar | PK |  | SI | Uso musc. Accesoria |
| QC1F41 | varchar | PK |  | SI | Sibilancias Audibles |
| QC1F42 | varchar | PK |  | SI | Cianosis |
| QC1F43 | varchar | PK |  | SI | Saturacion de Oxigeno |
| QC1F44 | varchar | PK |  | SI | Peso (kg.) |
| QC1F45 | varchar | PK |  | SI | Talla (cms.) |
| QC1F46 | varchar | PK |  | SI | IMC |
| QC1F47 | varchar | PK |  | SI | Escolaridad |
| QC1F48 | varchar | PK |  | SI | Vive Con |
| QC1F49 | varchar | PK |  | SI | Antecedentes laborales |
| QC1F5 | varchar | PK |  | SI | Calefacción |
| QC1F6 | varchar | PK |  | SI | Historia Asma Infancia |
| QC1F7 | varchar | PK |  | SI | Historia de tos o disnea con risa |
| QC1F8 | varchar | PK |  | SI | Historia de Sibilancia recurrente |
| QC1F9 | varchar | PK |  | SI | Alivio inmediato con B2 |
| QC2F1 | varchar | PK |  | SI | Nº/día |
| QC2F15 | varchar | PK |  | SI | Otro |
| QC2F16 | varchar | PK |  | SI | Otro |
| QC2F19 | varchar | PK |  | SI | Disnea |
| QC2F20 | varchar | PK |  | SI | Palpacion |
| QC2F3 | varchar | PK |  | SI | Años |
| QC2F4 | varchar | PK |  | SI | Años |
| QC2F5 | varchar | PK |  | SI | Años |
| QC3F1 | varchar | PK |  | SI | Años |
| QC3F19 | varchar | PK |  | SI | Expectoración |
| QC3F20 | varchar | PK |  | SI | Percusion |
| QC4F1 | varchar | PK |  | SI | Paquete/año |
| QC4F19 | varchar | PK |  | SI | Fiebre |
| QC4F20 | varchar | PK |  | SI | Auscultacion |
| QC5F19 | varchar | PK |  | SI | Dolor Toracico |
| QC6F19 | varchar | PK |  | SI | Caracteristicas |
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
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESPAPregnancyDR | bigint | PK | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint | PK | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar | PK | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar | PK | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
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