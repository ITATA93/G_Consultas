# SQLUser.LBC_PathogenPathogenicityRule

**Schema:** SQLUser
**Columnas:** 122
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCPAPR_ParRef | bigint | PK |  | NO | LBCPathogen Parent Reference |
| LBCPAPR_AdmType | varchar |  |  | SI | Admission Type
Compared with the value of Admissi... |
| LBCPAPR_AgeFrom | double |  |  | SI | Age Range From (format [yy].mmdd , ddd is 0-1231)... |
| LBCPAPR_AgeTo | double |  |  | SI | Age Range To (format [yy].mmdd , mmdd is 0-1231)
... |
| LBCPAPR_AnatomicalSiteQualifier_DR | varchar |  | FK | SI | [DEPRECATED]Anatomical Site Qualifier[/DEPRECATED] |
| LBCPAPR_AnatomicalSiteQualifiers | varchar |  |  | SI | Anatomical Site Qualifiers |
| LBCPAPR_AnatomicalSite_DR | bigint |  | FK | SI | [DEPRECATED]Anatomical Site[/DEPRECATED] |
| LBCPAPR_AnatomicalSites | varchar |  |  | SI | Anatomical Sites |
| LBCPAPR_AssignAntibioticPanel | varchar |  |  | SI | Assign Antibiotic Panel |
| LBCPAPR_ClinicalCondition_DR | bigint |  | FK | SI | Clinical Condition |
| LBCPAPR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCPAPR_DateFrom | date |  |  | SI | Effective date for the record |
| LBCPAPR_DateTo | date |  |  | SI | Last day the record is active  |
| LBCPAPR_Desc | varchar |  |  | NO | Description |
| LBCPAPR_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCPAPR_Lesion_DR | bigint |  | FK | SI | Lesion |
| LBCPAPR_PatType_DR | bigint |  | FK | SI | Patient Type |
| LBCPAPR_PathogenGrowthQualifier_DR | bigint |  | FK | SI | Organism Growth Qualifier |
| LBCPAPR_PathogenSubType_DR | varchar |  | FK | SI | Sub Type of Pathogen |
| LBCPAPR_Pregnant | varchar |  |  | SI | Pregnant. |
| LBCPAPR_RowID | varchar |  |  | NO | - |
| LBCPAPR_Sequence | numeric |  |  | SI | Priority  Sequence |
| LBCPAPR_Species | varchar |  |  | SI | Species |
| LBCPAPR_SpecimenGroup_DR | bigint |  | FK | SI | Specimen Group |
| LBCPAPR_Specimen_DR | bigint |  | FK | SI | Specimen |
| LBCPAPR_SubjectType_DR | bigint |  | FK | SI | Subject Type |
| LBCPAPR_Type | varchar |  |  | SI | Type |
| Q01 | - |  |  | SI | Asignación del Estipendio |
| Q02 | - |  |  | SI | Resultado Indice Barthel |
| Q02ObsDR | - |  |  | SI | Resultado Indice Barthel DR |
| Q03 | - |  |  | SI | Previsión |
| Q04 | - |  |  | SI | PRAIS |
| Q05 | - |  |  | SI | Chile Solidario |
| Q06 | - |  |  | SI | PASIS |
| Q07 | - |  |  | SI | Ficha Protección Social Menor a 8.500 pts. |
| Q08 | - |  |  | SI | Corresponde Estipendio |
| Q09 | - |  |  | SI | Asigna Estipendio |
| Q10 | - |  |  | SI | Antecedentes del cuidador |
| Q11 | - |  |  | SI | Rut Cuidador |
| Q12 | - |  |  | SI | Apellidos del Cuidador |
| Q13 | - |  |  | SI | Nombre del Cuidador |
| Q14 | - |  |  | SI | Fecha de Nacimiento del Cuidador |
| Q15 | - |  |  | SI | Género´del Cuidador |
| Q16 | - |  |  | SI | Estado Civil del Cuidador |
| Q17 | - |  |  | SI | Domicilio del Cuidador |
| Q18 | - |  |  | SI | Población/Villa |
| Q19 | - |  |  | SI | E-Mail |
| Q20 | - |  |  | SI | Escolaridad |
| Q21 | - |  |  | SI | Relación/Parentesco |
| Q22 | - |  |  | SI | Otro (Especifique) |
| Q23 | - |  |  | SI | Previsión del Cuidador |
| Q24 | - |  |  | SI | Teléfono Fijo |
| Q25 | - |  |  | SI | Celular |
| Q26 | - |  |  | SI | Postrado Oncológico |
| Q27 | - |  |  | SI | Programa alivio dolor |
| Q28 | - |  |  | SI | Uso oxigenoterapia |
| Q29 | - |  |  | SI | Oxigenoterapia Observaciones |
| Q30 | - |  |  | SI | Diáisis |
| Q31 | - |  |  | SI | Diálisis Observaciones |
| Q33 | - |  |  | SI | Condición sensorial |
| Q34 | - |  |  | SI | Estado de conciencia |
| Q35 | - |  |  | SI | Vías de comunicación |
| Q36 | - |  |  | SI | Alimentación |
| Q37 | - |  |  | SI | Cavidad bucal |
| Q38 | - |  |  | SI | Continencia |
| Q39 | - |  |  | SI | Formas de apoyo a incontinencia |
| Q40 | - |  |  | SI | Tendencia a fecalomas |
| Q41 | - |  |  | SI | Amputaciónes u ortesis |
| Q42 | - |  |  | SI | Estado nutricional |
| Q44 | - |  |  | SI | Prevención de UPP |
| Q45 | - |  |  | SI | Cantidad |
| Q46 | - |  |  | SI | Localización |
| Q47 | - |  |  | SI | Grado o tipo |
| Q48 | - |  |  | SI | Breve descripción |
| Q49 | - |  |  | SI | Factores de Riesgo Más Importantes |
| Q50 | - |  |  | SI | Aseo (Uñas) |
| Q51 | - |  |  | SI | Cortes (Uñas) |
| Q52 | - |  |  | SI | Alteraciones (Uñas) |
| Q60 | - |  |  | SI | Tipo de Pensión |
| Q61 | - |  |  | SI | Estado de Uñas |
| Q62 | - |  |  | SI | Presencia de Heridas |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*