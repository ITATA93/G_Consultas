# SQLUser.LB_RequestSpecimenContainerDetail

**Schema:** SQLUser
**Columnas:** 154
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBRQSPCDET_RowID | bigint | PK |  | NO | - |
| LBRQSPCDET_AnatomicalSite | varchar |  |  | SI | Specimen Container Anatomical Site |
| LBRQSPCDET_AnatomicalSiteQualifier | varchar |  |  | SI | Specimen Container Anatomical Site Qualifier |
| LBRQSPCDET_CollectedBy | varchar |  |  | SI | Specimen Container Collected By |
| LBRQSPCDET_CollectionCentre | varchar |  |  | SI | Specimen Container Collection Centre |
| LBRQSPCDET_CollectionDate | date |  |  | SI | Specimen Container Date Of Collection of the sampl... |
| LBRQSPCDET_CollectionTime | time |  |  | SI | Specimen Container Time Of Collection of the sampl... |
| LBRQSPCDET_Comments | varchar |  |  | SI | Specimen Container Comments |
| LBRQSPCDET_Container | varchar |  |  | SI | Specimen Container Container |
| LBRQSPCDET_ContainerNumber | varchar |  |  | SI | Specimen Container Container Number |
| LBRQSPCDET_Date | date |  |  | SI | Date of the record |
| LBRQSPCDET_Initiation | varchar |  |  | SI | Specimen Container Initiation |
| LBRQSPCDET_LabSite | varchar |  |  | SI | Specimen Container Lab Site |
| LBRQSPCDET_Lesion | varchar |  |  | SI | Specimen Container Lesion |
| LBRQSPCDET_ReceivedBy | varchar |  |  | SI | Specimen Container Received By |
| LBRQSPCDET_ReceivedDate | date |  |  | SI | Specimen Container Date Of Receiving |
| LBRQSPCDET_ReceivedTime | time |  |  | SI | Specimen Container Time Of Receiving |
| LBRQSPCDET_Specimen | varchar |  |  | SI | Specimen Container Specimen |
| LBRQSPCDET_SpecimenComment | varchar |  |  | SI | Specimen Container Specimen Comment |
| LBRQSPCDET_SpecimenContainer_DR | bigint |  | FK | SI | - |
| LBRQSPCDET_SpecimenNumber | varchar |  |  | SI | Specimen Container Specimen Number |
| LBRQSPCDET_TSDescription | varchar |  |  | SI | Specimen Container Test Set Description |
| LBRQSPCDET_Time | time |  |  | SI | Time of the record |
| LBRQSPCDET_VolumeCollected | varchar |  |  | SI | Specimen Container Volume Collected |
| LBRQSPCDET_VolumeCurrently | varchar |  |  | SI | Specimen Container Volume Currently  |
| Q01 | - |  |  | SI | FECHA DE INGRESO |
| Q02 | - |  |  | SI | HORA DE INGRESO |
| Q03 | - |  |  | SI | PROCEDENCIA |
| Q04 | - |  |  | SI | INFORMACIÓN ENTREGADA POR |
| Q05 | - |  |  | SI | ANAMNESIS PRÓXIMA |
| Q06 | - |  |  | SI | DETALLE DEL CUESTINARIO |
| Q07 | - |  |  | SI | EXAMEN FÍSICO UNIFICADO |
| Q08 | - |  |  | SI | CHEQUEO ANTECEDENTES |
| Q09 | - |  |  | SI | CAPACIDAD FUNCIONAL |
| Q10 | - |  |  | SI | HÁBITOS |
| Q11 | - |  |  | SI | RESPIRATORIO |
| Q12 | - |  |  | SI | CARDIOVASCULAR |
| Q13 | - |  |  | SI | DIGESTIVO |
| Q14 | - |  |  | SI | HEMATOLOGIA/ONCOLOGIA |
| Q15 | - |  |  | SI | ENFERMEDADES INFECCIOSAS |
| Q16 | - |  |  | SI | DIABETES |
| Q17 | - |  |  | SI | ENDOCRINOLOGIA y NUTRICIÓN |
| Q18 | - |  |  | SI | CABEZA Y CUELLO |
| Q19 | - |  |  | SI | REUMATOLOGIA |
| Q20 | - |  |  | SI | NEUROLOGIA |
| Q21 | - |  |  | SI | PSIQUIATRÍA |
| Q22 | - |  |  | SI | GENITOURINARIO |
| Q23 | - |  |  | SI | MEDICAMENTOS DE USO RECIENTE |
| Q24 | - |  |  | SI | EXAMEN FÍSICO GENERAL |
| Q25 | - |  |  | SI | ACTITUD |
| Q26 | - |  |  | SI | PIEL Y MUCOSAS |
| Q27 | - |  |  | SI | RESPIRACIÓN |
| Q28 | - |  |  | SI | ABDOMEN |
| Q29 | - |  |  | SI | peso |
| Q29ObsDR | - |  |  | SI | peso DR |
| Q30 | - |  |  | SI | talla |
| Q30ObsDR | - |  |  | SI | talla DR |
| Q31 | - |  |  | SI | temperatura |
| Q31ObsDR | - |  |  | SI | temperatura DR |
| Q32 | - |  |  | SI | frecuencia cardíaca |
| Q32ObsDR | - |  |  | SI | frecuencia cardíaca DR |
| Q33 | - |  |  | SI | frecuencia respiratoria |
| Q33ObsDR | - |  |  | SI | frecuencia respiratoria DR |
| Q34 | - |  |  | SI | presión arterial sistólica |
| Q34ObsDR | - |  |  | SI | presión arterial sistólica DR |
| Q35 | - |  |  | SI | presión arterial diastólica |
| Q35ObsDR | - |  |  | SI | presión arterial diastólica DR |
| Q36 | - |  |  | SI | presión arterial média |
| Q36ObsDR | - |  |  | SI | presión arterial média DR |
| Q37 | - |  |  | SI | saturación oxígeno |
| Q37ObsDR | - |  |  | SI | saturación oxígeno DR |
| Q38 | - |  |  | SI | EXAMEN FÍSICO GENERAL |
| Q39 | - |  |  | SI | EX. CABEZA Y CUELLO |
| Q40 | - |  |  | SI | CABEZA Y CUELLO |
| Q41 | - |  |  | SI | CABEZA Y CUELLO |
| Q42 | - |  |  | SI | EX. RESPIRATORIO |
| Q43 | - |  |  | SI | RESPIRATORIO |
| Q44 | - |  |  | SI | RESPIRATORIO |
| Q45 | - |  |  | SI | imagem |
| Q46 | - |  |  | SI | EX. CARDIOVASCULAR |
| Q47 | - |  |  | SI | NORMAL |
| Q48 | - |  |  | SI | ALTERACIONES DE RITMO |
| Q49 | - |  |  | SI | RUIDOS PATOLÓGICOS |
| Q50 | - |  |  | SI | CIRCULACIÓN CAPILAR |
| Q51 | - |  |  | SI | PULSOS PERIFÉRICOS DÉBILES O AUSENTES |
| Q52 | - |  |  | SI | EDEMA |
| Q53 | - |  |  | SI | CARDIOVASCULAR |
| Q54 | - |  |  | SI | EX. ABDOMEN |
| Q55 | - |  |  | SI | INSPECCIÓN |
| Q56 | - |  |  | SI | PALPACIÓN |
| Q57 | - |  |  | SI | VICEROMEGALIAS |
| Q58 | - |  |  | SI | CRUIDOS HIDROAÉREOS |
| Q59 | - |  |  | SI | CLOCALIZACIÓN DEL DOLOR |
| Q60 | - |  |  | SI | ABDOMEN |
| Q61 | - |  |  | SI | EX. NEUROLÓGICO |
| Q62 | - |  |  | SI | PUPILAS |
| Q63 | - |  |  | SI | HABLA |
| Q64 | - |  |  | SI | MOTOR |
| Q65 | - |  |  | SI | SENSIBILIDAD |
| Q66 | - |  |  | SI | REFLEJOS |
| Q67 | - |  |  | SI | SIGNOS MENÍNGEOS |
| Q68 | - |  |  | SI | NEUROLÓGICO |
| Q69 | - |  |  | SI | EX. GENITAL Y PELVIANO |
| Q70 | - |  |  | SI | GENITAL Y PELVIANO |
| Q71 | - |  |  | SI | EX. MÚSCULO ESQUELÉTICO |
| Q72 | - |  |  | SI | MÚSCULO ESQUELÉTICO |
| Q73 | - |  |  | SI | CONCLUSIÓN |
| Q74 | - |  |  | SI | CONCLUSIÓN |
| Q75 | - |  |  | SI | PLAN |
| Q76 | - |  |  | SI | PLAN |
| Q77 | - |  |  | SI | CHEQUEO DE ANTECEDENTES |
| Q78 | - |  |  | SI | EXAMENES DE LABORATORIO PERTINENTES |
| Q79 | - |  |  | SI | EXAMENES DE IMAGEN PERTINENTES |
| Q80 | - |  |  | SI | EXAMENES COMPLEMENTARIOS OTROS |
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