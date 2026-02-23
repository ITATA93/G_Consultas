# questionnaire.QCLXXTQ01

**Schema:** questionnaire
**Columnas:** 116
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario Regional Chile**. Formulario de evaluación clínica adaptado para Chile.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | Síntomas Constitucionales |
| Q02 | varchar | PK |  | SI | Fatiga |
| Q03 | varchar | PK |  | SI | Fiebre |
| Q04 | varchar | PK |  | SI | Hipotermia |
| Q05 | varchar | PK |  | SI | Insomnio |
| Q06 | varchar | PK |  | SI | Obesidad |
| Q07 | varchar | PK |  | SI | Olor (olor del paciente) |
| Q08 | varchar | PK |  | SI | Espasmo / Escalofriós |
| Q09 | varchar | PK |  | SI | Sudoración |
| Q10 | varchar | PK |  | SI | Aumento de Peso |
| Q11 | varchar | PK |  | SI | Pérdida de Peso |
| Q12 | varchar | PK |  | SI | Otros Síntomas Constitucionales |
| Q13 | varchar | PK |  | SI | Anorexia |
| Q14 | varchar | PK |  | SI | Ascitis no neoplásica |
| Q15 | varchar | PK |  | SI | Colitis |
| Q16 | varchar | PK |  | SI | Constipación |
| Q17 | varchar | PK |  | SI | Deshidratación |
| Q18 | varchar | PK |  | SI | Dentales (prótesis dentarias) |
| Q19 | varchar | PK |  | SI | Dentales (enfermedad periodontal) |
| Q20 | varchar | PK |  | SI | Dentales (piezas dentarias) |
| Q21 | varchar | PK |  | SI | Diarrea |
| Q22 | varchar | PK |  | SI | Distensión abdominal |
| Q23 | varchar | PK |  | SI | Xerostomía (sequedad bucal, défici saliva) |
| Q24 | varchar | PK |  | SI | Diafagia |
| Q25 | varchar | PK |  | SI | Enteritis |
| Q26 | varchar | PK |  | SI | Esofagitis |
| Q27 | varchar | PK |  | SI | Fistulas |
| Q28 | varchar | PK |  | SI | Flatulencia |
| Q29 | varchar | PK |  | SI | Gastritis |
| Q30 | varchar | PK |  | SI | Dispepsia |
| Q31 | varchar | PK |  | SI | Hemorroides |
| Q32 | varchar | PK |  | SI | Ileo |
| Q33 | varchar | PK |  | SI | Incontinencia anal |
| Q34 | varchar | PK |  | SI | Filtración o fuga |
| Q35 | varchar | PK |  | SI | Malabsorción |
| Q36 | varchar | PK |  | SI | Mucositis o estomatitis clínica |
| Q37 | varchar | PK |  | SI | Mucositis o estomatitis funcional |
| Q38 | varchar | PK |  | SI | Náuseas |
| Q39 | varchar | PK |  | SI | Necrosis |
| Q40 | varchar | PK |  | SI | Obstrucción del tubo digestivo |
| Q41 | varchar | PK |  | SI | Perforación del tubo digestivo |
| Q42 | varchar | PK |  | SI | Proctitis |
| Q43 | varchar | PK |  | SI | Prolapso de ostomía digestiva |
| Q44 | varchar | PK |  | SI | Cambios o alteraciones salivales |
| Q45 | varchar | PK |  | SI | Estenosis o estrechez del tubo digestivo |
| Q46 | varchar | PK |  | SI | Disgeusia (alteraciones del gusto) |
| Q47 | varchar | PK |  | SI | Tiflitis |
| Q48 | varchar | PK |  | SI | Úlceras |
| Q49 | varchar | PK |  | SI | Vómitos |
| Q50 | varchar | PK |  | SI | Otros eventos gastrointestinales |
| Q51 | varchar | PK |  | SI | Colecistitis |
| Q52 | varchar | PK |  | SI | Disfunción o insuficiencia hepática |
| Q53 | varchar | PK |  | SI | Deficiencia pancreática exógena |
| Q54 | varchar | PK |  | SI | Pancreatitis |
| Q55 | varchar | PK |  | SI | Otras alteraciones hepatobiliares o pancreáticas |
| Q56 | varchar | PK |  | SI | Pancreatitis |
| Q57 | varchar | PK |  | SI | Otras alteraciones hepatobiliares o pancreáticas |
| Q58 | varchar | PK |  | SI | Celularidad de la MO |
| Q59 | varchar | PK |  | SI | Recuento de linfocitos T CD4+ |
| Q60 | varchar | PK |  | SI | Haptoglobina |
| Q61 | varchar | PK |  | SI | Hemólisis |
| Q62 | varchar | PK |  | SI | Sobrecarga de Hierro |
| Q63 | varchar | PK |  | SI | Leucocitosis |
| Q64 | varchar | PK |  | SI | Linfopenia |
| Q65 | varchar | PK |  | SI | Mielodisplasia |
| Q66 | varchar | PK |  | SI | Neutrófilos, granulocitos |
| Q67 | varchar | PK |  | SI | Plaquetas |
| Q68 | varchar | PK |  | SI | Función esplénica |
| Q69 | varchar | PK |  | SI | Otros eventos hematológicos |
| Q70 | varchar | PK |  | SI | CID |
| Q71 | varchar | PK |  | SI | Fibrinógeno |
| Q72 | varchar | PK |  | SI | RIN |
| Q73 | varchar | PK |  | SI | Tiempo parcial de tromboplastina |
| Q74 | varchar | PK |  | SI | Microangiopatía trombótica |
| Q75 | varchar | PK |  | SI | Otros eventos sobre la coagulación |
| Q76 | varchar | PK |  | SI | Eventos adversos Gastroenterológicos |
| Q77 | varchar | PK |  | SI | Eventos adversos Hematológicos |
| Q78 | varchar | PK |  | SI | Xerostomía (sequedad bucal, déficit saliva) |
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