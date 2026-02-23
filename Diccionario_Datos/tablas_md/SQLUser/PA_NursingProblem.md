# SQLUser.PA_NursingProblem

**Schema:** SQLUser
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NPParRef | bigint | PK |  | NO | - |
| NP_Childsub | double |  |  | NO | - |
| NP_NRCProb_DR | bigint |  | FK | SI | - |
| NP_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | 1. DEPENDIENTES DEL PACIENTE |
| Q02 | - |  |  | SI | 1.1 ANTECEDENTES |
| Q03 | - |  |  | SI | Paciente es niño/a o adolescente |
| Q04 | - |  |  | SI | Paciente es profesional sanitario |
| Q05 | - |  |  | SI | Rol socio-familiar que desempeña el/la paciente |
| Q06 | - |  |  | SI | Paciente presenta discapacidad física, psíquica o ... |
| Q07 | - |  |  | SI | Paciente presenta problemas de adicción recientes ... |
| Q08 | - |  |  | SI | Enfermedad mental previa |
| Q09 | - |  |  | SI | 1.2 SITUACIÓN CLÍNICA |
| Q10 | - |  |  | SI | Síntomas de difícil control |
| Q11 | - |  |  | SI | Síntomas refractarios |
| Q12 | - |  |  | SI | Situaciones urgentes en paciente terminal oncológi... |
| Q13 | - |  |  | SI | Situación de últimos días de difícil control |
| Q14 | - |  |  | SI | Situaciones clínicas secundarias a progresión tumo... |
| Q15 | - |  |  | SI | Descompensación aguda en insuficiencia de órgano e... |
| Q16 | - |  |  | SI | Trastorno cognitivo severo |
| Q17 | - |  |  | SI | Cambio brusco en el nivel de autonomía funcional |
| Q18 | - |  |  | SI | Existencia de comorbilidad de difícil control |
| Q19 | - |  |  | SI | Síndrome constitucional severo |
| Q20 | - |  |  | SI | Difícil manejo clínico por incumplimiento terapéut... |
| Q21 | - |  |  | SI | 1.3 SITUACIÓN PSICO-EMOCIONAL |
| Q22 | - |  |  | SI | Paciente presenta riesgo de suicidio |
| Q23 | - |  |  | SI | Paciente solicita adelantar el proceso de la muert... |
| Q24 | - |  |  | SI | Paciente presenta angustia existencial y/o sufrimi... |
| Q25 | - |  |  | SI | Conflicto en la comunicación entre paciente y fami... |
| Q26 | - |  |  | SI | Conflicto en la comunicación entre paciente y equi... |
| Q27 | - |  |  | SI | Paciente presenta afrontamiento emocional desadapt... |
| Q28 | - |  |  | SI | 2. DEPENDIENTES DE LA FAMILIA Y EL ENTORNO |
| Q29 | - |  |  | SI | Ausencia o insuficiencia de soporte familiar y/o c... |
| Q30 | - |  |  | SI | Familiares y/o cuidadores no competentes para el c... |
| Q31 | - |  |  | SI | Familia disfuncional |
| Q32 | - |  |  | SI | Claudicación familiar |
| Q33 | - |  |  | SI | Duelos complejos |
| Q34 | - |  |  | SI | Limitaciones estructurales del entorno |
| Q35 | - |  |  | SI | 3. DEPENDIENTES DE LA ORGANIZACIÓN SANITARIA |
| Q36 | - |  |  | SI | 3.1 PROFESIONAL / EQUIPO |
| Q37 | - |  |  | SI | Aplicación de sedación paliativa de manejo difícil |
| Q38 | - |  |  | SI | Dificultades para la indicación y/o manejo de fárm... |
| Q39 | - |  |  | SI | Dificultades para la indicación y/o manejo de inte... |
| Q40 | - |  |  | SI | Limitaciones en la competencia profesional por el ... |
| Q41 | - |  |  | SI | 3.2 RECURSOS |
| Q42 | - |  |  | SI | Dificultades para la gestión de necesidades de téc... |
| Q43 | - |  |  | SI | Dificultades para la gestión y/o manejo de necesid... |
| Q44 | - |  |  | SI | Nivel de Complejidad |
| Q45 | - |  |  | SI | C: Compleja |
| Q46 | - |  |  | SI | AC: Altamente Compleja |
| Q47 | - |  |  | SI | Situación |
| Q48 | - |  |  | SI | Intervención de los Recursos Avanzados / Específic... |
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