# SQLUser.OE_Escalation

**Schema:** SQLUser
**Columnas:** 106
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OEESC_RowId | bigint | PK |  | NO | - |
| OEESC_ContactMethod | varchar |  |  | SI | Contact Method |
| OEESC_EscalationDate | date |  |  | SI | Escalation Date |
| OEESC_EscalationLevel_DR | bigint |  | FK | SI | Des Ref EscalationLevel |
| OEESC_EscalationTime | time |  |  | SI | Escalation Time |
| OEESC_HeadOfDeptGroup_DR | varchar |  | FK | SI | Des Ref HeadOfDeptGroup |
| OEESC_HeadOfDept_DR | bigint |  | FK | SI | Des Ref HeadOfDept |
| OEESC_HeadOfDivision_DR | varchar |  | FK | SI | Des Ref HeadOfDivision |
| OEESC_MainCareProvider_DR | varchar |  | FK | SI | Des Ref MainCareProvider |
| OEESC_MedicalSuperintendent_DR | varchar |  | FK | SI | Des Ref MedicalSuperintendent |
| OEESC_OrderItem_DR | varchar |  | FK | SI | Des Ref OrderItem |
| OEESC_ServiceProvider | varchar |  |  | SI | External Info System |
| Q01 | - |  |  | SI | Edad |
| Q02 | - |  |  | SI | Género |
| Q03 | - |  |  | SI | Diagnóstico |
| Q04 | - |  |  | SI | Deterioro cognitivo |
| Q05 | - |  |  | SI | Factores ambientales |
| Q06 | - |  |  | SI | Cirugía / sedación / anestesia |
| Q07 | - |  |  | SI | Medicación |
| Q08 | - |  |  | SI | Indicación para la evaluación |
| Q09 | - |  |  | SI | Intervenciones |
| Q10 | - |  |  | SI | 7-11: Bajo riesgo |
| Q11 | - |  |  | SI | >=12: Alto riesgo |
| Q12 | - |  |  | SI | Permite al equipo clínico evaluar rápida y fácilme... |
| Q13 | - |  |  | SI | 7 - 11 |
| Q14 | - |  |  | SI | Bajo riesgo |
| Q15 | - |  |  | SI | ≥12 |
| Q16 | - |  |  | SI | Alto riesgo |
| Q17 | - |  |  | SI | Puntaje |
| Q18 | - |  |  | SI | Clasificación |
| Q19 | - |  |  | SI | * Medicamentos: Sedantes (excluyendo pacientes de ... |
| Q20 | - |  |  | SI | Fecha |
| Q21 | - |  |  | SI | Hora |
| Q22 | - |  |  | SI | Other indication |
| Q23 | - |  |  | SI | Guidelines |
| Q24 | - |  |  | SI | Assess and periodically reassess each  patient’s r... |
| Q25 | - |  |  | SI | Educate child / parent / guardian / boarder on : |
| Q26 | - |  |  | SI | * potential falls risk and interventions |
| Q27 | - |  |  | SI | * call bell and light use |
| Q28 | - |  |  | SI | * bed side/cot rails use |
| Q29 | - |  |  | SI | * appropriate clothing and non-slip footwear |
| Q30 | - |  |  | SI | Place child in appropriately sized bed with brakes... |
| Q31 | - |  |  | SI | Ensure mobility aids and call bell within reach. |
| Q32 | - |  |  | SI | Routine Care Instructions : |
| Q33 | - |  |  | SI | * Assess toileting and assist as needed |
| Q34 | - |  |  | SI | * Head and foot ends placed on beds |
| Q35 | - |  |  | SI | * If child mobilises with IV pole, ensure equipmen... |
| Q36 | - |  |  | SI | * Environment is clear of clutter and trip hazards |
| Q37 | - |  |  | SI | * Curtains and room door open, unless otherwise in... |
| Q38 | - |  |  | SI | * Ensure adequate lighting and leave nightlight on... |
| Q39 | - |  |  | SI | Additional considerations for high risk patients (... |
| Q40 | - |  |  | SI | * Paediatric High Falls sign added to bedside |
| Q41 | - |  |  | SI | * Hourly visual checks on patient |
| Q42 | - |  |  | SI | * Assist with ambulation |
| Q43 | - |  |  | SI | * Consider moving child closer to nurses' station |
| Q44 | - |  |  | SI | * Assess need for 1:1 supervision |
| Q45 | - |  |  | SI | Assess need for 1:1 supervision |
| Q46 | - |  |  | SI | * Review medication administration times |
| Q47 | - |  |  | SI | * Engage parents / carers / boarders in falls prev... |
| Q48 | - |  |  | SI | Age |
| Q49 | - |  |  | SI | In the 2009 study (J Spec Pediatr Nurs 2009 |
| Q50 | - |  |  | SI | and a negative predictive value of 63% for the pre... |
| Q51 | - |  |  | SI | References |
| Q52 | - |  |  | SI | 1. Hill‐Rodriguez D, Messmer PR, Williams PD, Zell... |
| Q53 | - |  |  | SI | 1. Hill-Rodriguez D, Messmer PR, Wood ML. Humpty D... |
| Q54 | - |  |  | SI | 2. Hill‐Rodriguez D, Messmer PR, Williams PD, Zell... |
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