# questionnaire.QTCECPSEG

> SEGUIMIENTO - Protocolo Estandarizado de Registro de Visita Domiciliaria Integral

**Schema:** questionnaire
**Columnas:** 128
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* SEGUIMIENTO - Protocolo Estandarizado de Registro de Visita Domiciliaria Integral

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | varchar |  |  | SI | Creencia Religiosa |
| Q10 | varchar |  |  | SI | Fono |
| Q11 | varchar |  |  | SI | Permanece en pieza |
| Q12 | varchar |  |  | SI | Nº de Personas que duermen en la misma habitación |
| Q13 | varchar |  |  | SI | La cama es solo para el Paciente? |
| Q14 | varchar |  |  | SI | Condiciones de la vivienda |
| Q15 | varchar |  |  | SI | Conocimiento de la atención y cuidados por parte d... |
| Q16 | varchar |  |  | SI | Escolaridad |
| Q17 | varchar |  |  | SI | Calidad Laboral |
| Q18 | varchar |  |  | SI | Apoyo |
| Q19 | varchar |  |  | SI | Diagnóstico |
| Q2 | bit |  |  | SI | Activo |
| Q20 | varchar |  |  | SI | Tratamiento |
| Q21 | varchar |  |  | SI | Grado de Cumplimiento |
| Q22 | varchar |  |  | SI | Revisión de Farmacos |
| Q23 | varchar |  |  | SI | Retiro de Farmacos |
| Q24 | varchar |  |  | SI | Presión Arteria Sistolica |
| Q24ObsDR | varchar |  | FK | SI | Presión Arteria Sistolica DR |
| Q25 | varchar |  |  | SI | PA2 |
| Q25ObsDR | varchar |  | FK | SI | PA2 DR |
| Q26 | varchar |  |  | SI | P |
| Q27 | varchar |  |  | SI | FR |
| Q27ObsDR | varchar |  | FK | SI | FR DR |
| Q28 | varchar |  |  | SI | Tº |
| Q28ObsDR | varchar |  | FK | SI | Tº DR |
| Q3 | bit |  |  | SI | Pasivo |
| Q30 | varchar |  |  | SI | PS |
| Q31 | varchar |  |  | SI | Indice de Norton |
| Q32 | varchar |  |  | SI | Oxigeno |
| Q32ObsDR | varchar |  | FK | SI | Oxigeno DR |
| Q33 | bit |  |  | SI | S |
| Q34 | bit |  |  | SI | V |
| Q35 | bit |  |  | SI | N |
| Q36 | bit |  |  | SI | SV |
| Q37 | bit |  |  | SI | SN |
| Q39 | bit |  |  | SI | SVN |
| Q4 | bit |  |  | SI | Conyuge |
| Q40 | bit |  |  | SI | Permanente |
| Q41 | bit |  |  | SI | Esporádico |
| Q42 | varchar |  |  | SI | Paciente |
| Q43 | varchar |  |  | SI | Familia |
| Q44 | bit |  |  | SI | Obeso |
| Q45 | bit |  |  | SI | Enflaquecido |
| Q46 | bit |  |  | SI | Eutrófico |
| Q47 | bit |  |  | SI | Caquéxico |
| Q48 | varchar |  |  | SI | Hidratación |
| Q49 | varchar |  |  | SI | Alimentación |
| Q5 | bit |  |  | SI | Hijos |
| Q50 | varchar |  |  | SI | Observación |
| Q51 | bit |  |  | SI | Tranquilo |
| Q52 | bit |  |  | SI | Ansioso |
| Q53 | bit |  |  | SI | Optimista |
| Q54 | bit |  |  | SI | Irritable |
| Q55 | bit |  |  | SI | Activo |
| Q56 | bit |  |  | SI | Pasivo |
| Q57 | bit |  |  | SI | Pesimista |
| Q58 | bit |  |  | SI | Depresivo |
| Q59 | bit |  |  | SI | Dependiente |
| Q60 | bit |  |  | SI | Autönomo |
| Q61 | bit |  |  | SI | Otros |
| Q62 | bit |  |  | SI | Decaimiento |
| Q63 | bit |  |  | SI | Letargo |
| Q64 | bit |  |  | SI | Anorexia |
| Q65 | bit |  |  | SI | Náuseas |
| Q66 | bit |  |  | SI | Vómito |
| Q67 | bit |  |  | SI | Estitiquez |
| Q68 | bit |  |  | SI | Gastraigia |
| Q69 | bit |  |  | SI | Disfagia |
| Q7 | bit |  |  | SI | Padres |
| Q70 | bit |  |  | SI | Mareos |
| Q71 | bit |  |  | SI | Diarrea |
| Q72 | bit |  |  | SI | Temblor |
| Q73 | bit |  |  | SI | Insomnio |
| Q74 | varchar |  |  | SI | Otros |
| Q75 | varchar |  |  | SI | El paciente se encuentra |
| Q76 | varchar |  |  | SI | Valoración del Paciente |
| Q77 | varchar |  |  | SI | Intervención/Actividad/Procedimiento |
| Q78 | varchar |  |  | SI | Insumos Entregados |
| Q79 | varchar |  |  | SI | Derivación |
| Q8 | varchar |  |  | SI | Otros |
| Q80 | varchar |  |  | SI | Responsable |
| Q81 | varchar |  |  | SI | Estamento |
| Q82 | varchar |  |  | SI | Voluntario |
| Q83 | varchar |  |  | SI | EVA |
| Q83ObsDR | varchar |  | FK | SI | EVA DR |
| Q84 | varchar |  |  | SI | Localizacion del Dolor |
| Q9 | varchar |  |  | SI | Cuidador Principal |
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