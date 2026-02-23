# SQLUser.MRC_PatientCondition

**Schema:** SQLUser
**Columnas:** 143
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| COND_RowId | bigint | PK |  | NO | - |
| COND_Code | varchar |  |  | NO | Code |
| COND_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| COND_CreatedDate | date |  |  | SI | Created Date |
| COND_CreatedTime | time |  |  | SI | Created Time |
| COND_CreatedUser_DR | bigint |  | FK | SI | Created User |
| COND_DateFrom | date |  |  | SI | Date From |
| COND_DateTo | date |  |  | SI | Date To |
| COND_Desc | varchar |  |  | NO | Description |
| COND_IconName | varchar |  |  | SI | IconName |
| COND_IconPriority | varchar |  |  | SI | IconPriority |
| COND_Owner | varchar |  |  | SI | Owner |
| COND_UpdatedDate | date |  |  | SI | Updated Date |
| COND_UpdatedTime | time |  |  | SI | Updated Time |
| COND_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Creencia Religiosa |
| Q10 | - |  |  | SI | Fono |
| Q11 | - |  |  | SI | Permanece en pieza |
| Q12 | - |  |  | SI | Nº de Personas que duermen en la misma habitación |
| Q13 | - |  |  | SI | La cama es solo para el Paciente? |
| Q14 | - |  |  | SI | Condiciones de la vivienda |
| Q15 | - |  |  | SI | Conocimiento de la atención y cuidados por parte d... |
| Q16 | - |  |  | SI | Escolaridad |
| Q17 | - |  |  | SI | Calidad Laboral |
| Q18 | - |  |  | SI | Apoyo |
| Q19 | - |  |  | SI | Diagnóstico |
| Q2 | - |  |  | SI | Activo |
| Q20 | - |  |  | SI | Tratamiento |
| Q21 | - |  |  | SI | Grado de Cumplimiento |
| Q22 | - |  |  | SI | Revisión de Farmacos |
| Q23 | - |  |  | SI | Retiro de Farmacos |
| Q24 | - |  |  | SI | PA |
| Q24ObsDR | - |  |  | SI | PA DR |
| Q25 | - |  |  | SI | PA2 |
| Q25ObsDR | - |  |  | SI | PA2 DR |
| Q26 | - |  |  | SI | P |
| Q27 | - |  |  | SI | FR |
| Q27ObsDR | - |  |  | SI | FR DR |
| Q28 | - |  |  | SI | Tº |
| Q28ObsDR | - |  |  | SI | Tº DR |
| Q29 | - |  |  | SI | EVA |
| Q29ObsDR | - |  |  | SI | EVA DR |
| Q3 | - |  |  | SI | Pasivo |
| Q30 | - |  |  | SI | PS |
| Q31 | - |  |  | SI | Indice de Norton |
| Q32 | - |  |  | SI | Oxigeno |
| Q32ObsDR | - |  |  | SI | Oxigeno DR |
| Q33 | - |  |  | SI | S |
| Q34 | - |  |  | SI | V |
| Q35 | - |  |  | SI | N |
| Q36 | - |  |  | SI | SV |
| Q37 | - |  |  | SI | SN |
| Q39 | - |  |  | SI | SVN |
| Q4 | - |  |  | SI | Conyuge |
| Q40 | - |  |  | SI | Permanente |
| Q41 | - |  |  | SI | Esporádico |
| Q42 | - |  |  | SI | Paciente |
| Q43 | - |  |  | SI | Familia |
| Q44 | - |  |  | SI | Obeso |
| Q45 | - |  |  | SI | Enflaquecido |
| Q46 | - |  |  | SI | Eutrófico |
| Q47 | - |  |  | SI | Caquéxico |
| Q48 | - |  |  | SI | Hidratación |
| Q49 | - |  |  | SI | Alimentación |
| Q5 | - |  |  | SI | Hijos |
| Q50 | - |  |  | SI | Observación |
| Q51 | - |  |  | SI | Tranquilo |
| Q52 | - |  |  | SI | Ansioso |
| Q53 | - |  |  | SI | Optimista |
| Q54 | - |  |  | SI | Irritable |
| Q55 | - |  |  | SI | Activo |
| Q56 | - |  |  | SI | Pasivo |
| Q57 | - |  |  | SI | Pesimista |
| Q58 | - |  |  | SI | Depresivo |
| Q59 | - |  |  | SI | Dependiente |
| Q60 | - |  |  | SI | Autönomo |
| Q61 | - |  |  | SI | Otros |
| Q62 | - |  |  | SI | Decaimiento |
| Q63 | - |  |  | SI | Letargo |
| Q64 | - |  |  | SI | Anorexia |
| Q65 | - |  |  | SI | Náuseas |
| Q66 | - |  |  | SI | Vómito |
| Q67 | - |  |  | SI | Estitiquez |
| Q68 | - |  |  | SI | Gastraigia |
| Q69 | - |  |  | SI | Disfagia |
| Q7 | - |  |  | SI | Padres |
| Q70 | - |  |  | SI | Mareos |
| Q71 | - |  |  | SI | Diarrea |
| Q72 | - |  |  | SI | Temblor |
| Q73 | - |  |  | SI | Insomnio |
| Q74 | - |  |  | SI | Otros |
| Q75 | - |  |  | SI | El paciente se encuentra |
| Q76 | - |  |  | SI | Valoración del Paciente |
| Q77 | - |  |  | SI | Intervención/Actividad/Procedimiento |
| Q78 | - |  |  | SI | Insumos Entregados |
| Q79 | - |  |  | SI | Derivación |
| Q8 | - |  |  | SI | Otros |
| Q80 | - |  |  | SI | Responsable |
| Q81 | - |  |  | SI | Estamento |
| Q82 | - |  |  | SI | Voluntario |
| Q83 | - |  |  | SI | EVA |
| Q84 | - |  |  | SI | Localizacion del Dolor |
| Q9 | - |  |  | SI | Cuidador Principal |
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