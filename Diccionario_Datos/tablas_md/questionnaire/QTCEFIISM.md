# questionnaire.QTCEFIISM

**Schema:** questionnaire
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | Escolaridad |
| Q02 | varchar | PK |  | SI | Ocupación |
| Q03 | varchar | PK |  | SI | Religión |
| Q04 | varchar | PK |  | SI | Adulto Responsable |
| Q05 | varchar | PK |  | SI | Motivo de Ingreso |
| Q06 | varchar | PK |  | SI | Enfermedad y/o Problema actual |
| Q07 | date | PK |  | SI | Fecha de Nacimiento |
| Q08 | varchar | PK |  | SI | Condiciones del Parto |
| Q09 | varchar | PK |  | SI | Desarrollo Psicomotor |
| Q10 | varchar | PK |  | SI | Antecedentes mórbidos |
| Q11 | varchar | PK |  | SI | Alergias |
| Q12 | varchar | PK |  | SI | Personalidad Previa |
| Q13 | varchar | PK |  | SI | Antecedentes Psiquiátricos |
| Q14 | varchar | PK |  | SI | Hospitalizaciones Psiquiátricas (Número y fecha de... |
| Q15 | varchar | PK |  | SI | Presión arterial |
| Q16 | varchar | PK |  | SI | Pulso |
| Q17 | varchar | PK |  | SI | Temp. |
| Q18 | varchar | PK |  | SI | Peso |
| Q19 | varchar | PK |  | SI | Higiene |
| Q20 | varchar | PK |  | SI | Nutrición e Hidratación |
| Q21 | varchar | PK |  | SI | Control esfínteres |
| Q22 | varchar | PK |  | SI | Cabeza - cuello |
| Q23 | varchar | PK |  | SI | Tórax |
| Q24 | varchar | PK |  | SI | Abdomen |
| Q25 | varchar | PK |  | SI | Extremidades |
| Q26 | varchar | PK |  | SI | Estado general y otras observaciones |
| Q27 | varchar | PK |  | SI | Examen neurológico |
| Q28 | varchar | PK |  | SI | Aspecto o biotipo |
| Q29 | varchar | PK |  | SI | Actitud al examen |
| Q30 | varchar | PK |  | SI | Cuidado personal |
| Q31 | varchar | PK |  | SI | Lúcido |
| Q32 | varchar | PK |  | SI | Obnubilado |
| Q33 | varchar | PK |  | SI | Enturbiado |
| Q34 | varchar | PK |  | SI | Estrechez |
| Q35 | varchar | PK |  | SI | ALT. CUANTITATIVA |
| Q36 | varchar | PK |  | SI | ALT. CUALITATIVA |
| Q37 | varchar | PK |  | SI | ALT. CUANTITATIVA |
| Q38 | varchar | PK |  | SI | ALT. CUALITATIVA |
| Q39 | varchar | PK |  | SI | ALT. CUANTITATIVA |
| Q40 | varchar | PK |  | SI | ALT. CUALITATIVA |
| Q41 | varchar | PK |  | SI | ALT. FORMAL |
| Q42 | varchar | PK |  | SI | ALT. CONTENIDO |
| Q43 | varchar | PK |  | SI | Inteligencia |
| Q44 | varchar | PK |  | SI | ALT. DE REACCIONES AFECTIVAS |
| Q45 | varchar | PK |  | SI | ALT. DEL ESTADO FUNDAMENTAL DEL ÁNIMO |
| Q46 | varchar | PK |  | SI | ALT. DE ASOCIACIONES AFECTIVAS |
| Q47 | varchar | PK |  | SI | ALT. CUANTITATIVA |
| Q48 | varchar | PK |  | SI | ALT. CUALITATIVA |
| Q49 | varchar | PK |  | SI | ALT. CURSO ACTO VOLUTIVO |
| Q50 | varchar | PK |  | SI | Hipótesis diagnóstica |
| Q51 | varchar | PK |  | SI | Objetivos terapéuticos |
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