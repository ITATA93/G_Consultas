# SQLUser.PA_ORAnaestAirwayCircuitSnapshot

**Schema:** SQLUser
**Columnas:** 113
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACIRC_ParRef | bigint | PK |  | NO | PA_ORAnaestSnapshot Parent Reference |
| ChildQ12DR | - |  |  | SI | Child Reference: Listado Tipo de Parto |
| PACIRC_ChildSub | double |  |  | NO | ChildSub |
| PACIRC_RowId | varchar |  |  | NO | - |
| PACIRC_Type_DR | bigint |  | FK | SI | Des Ref ORCAirwayCircuit |
| Q01 | - |  |  | SI | Antecedentes del Embarazo (RN Traslado) |
| Q02 | - |  |  | SI | Nombre de la Madre |
| Q03 | - |  |  | SI | Edad Materna |
| Q04 | - |  |  | SI | Fórmula Obstétrica |
| Q05 | - |  |  | SI | N° Gestaciones |
| Q06 | - |  |  | SI | N° Partos |
| Q07 | - |  |  | SI | N° Nacidos vivos |
| Q08 | - |  |  | SI | Grupo Sanguíneo Materno |
| Q10 | - |  |  | SI | Medicamentos que tomó durante el embarazo |
| Q11 | - |  |  | SI | Antecedentes del Parto (RN Traslado) |
| Q13 | - |  |  | SI | Indicación Parto Operatorio |
| Q14 | - |  |  | SI | Causa de Fórceps |
| Q15 | - |  |  | SI | Lugar del parto |
| Q16 | - |  |  | SI | Otro Lugar de Parto |
| Q19 | - |  |  | SI | Otra Anestesia (Parto) |
| Q20 | - |  |  | SI | Líquido Amniótico |
| Q21 | - |  |  | SI | Condición de la placenta |
| Q22 | - |  |  | SI | Circular de Cordón |
| Q24 | - |  |  | SI | Otras Complicaciones en el Trabajo de Parto |
| Q26 | - |  |  | SI | Detalle complicaciones del puerperio inmediato |
| Q27 | - |  |  | SI | Complicaciones Fetales |
| Q28 | - |  |  | SI | Otra complicación |
| Q29 | - |  |  | SI | Nacimiento y Atención Inmediata (RN Traslado) |
| Q30 | - |  |  | SI | Obstetricia |
| Q31 | - |  |  | SI | Fecha Nacimiento |
| Q32 | - |  |  | SI | Hora de Nacimiento |
| Q33 | - |  |  | SI | Sexo |
| Q34 | - |  |  | SI | Peso al Nacer |
| Q34ObsDR | - |  |  | SI | Peso al Nacer DR |
| Q35 | - |  |  | SI | Talla al Nacer |
| Q35ObsDR | - |  |  | SI | Talla al Nacer DR |
| Q36 | - |  |  | SI | Circunferencia Craneana |
| Q36ObsDR | - |  |  | SI | Circunferencia Craneana DR |
| Q37 | - |  |  | SI | Resultado |
| Q38 | - |  |  | SI | Semanas de gestación |
| Q39 | - |  |  | SI | Adecuación |
| Q40 | - |  |  | SI | Presentación |
| Q41 | - |  |  | SI | Contacto piel con piel |
| Q42 | - |  |  | SI | Tiempo Ininterrumpido de Contacto Piel a Piel (min... |
| Q43 | - |  |  | SI | Neonatología |
| Q44 | - |  |  | SI | Deposiciones |
| Q45 | - |  |  | SI | Lactancia Materna |
| Q46 | - |  |  | SI | Alimentación Complementaria |
| Q47 | - |  |  | SI | Administración Vacuna BCG |
| Q48 | - |  |  | SI | Administración Vitamina K |
| Q49 | - |  |  | SI | Profilaxis Ocular |
| Q50 | - |  |  | SI | Reanimación |
| Q51 | - |  |  | SI | Anomalía Congénita |
| Q52 | - |  |  | SI | Muestra de Sangre de Cordón Grupo RH Coomb |
| Q53 | - |  |  | SI | Morbilidad RN |
| Q54 | - |  |  | SI | Apgar |
| Q55 | - |  |  | SI | Apgar 1 Minuto |
| Q56 | - |  |  | SI | Apgar 5 Minutos |
| Q57 | - |  |  | SI | Apgar 10 Minutos |
| Q58 | - |  |  | SI | Comentarios y Observaciones |
| Q59 | - |  |  | SI | Información General (RN Traslado) |
| Q60 | - |  |  | SI | Fecha de Digitación |
| Q61 | - |  |  | SI | Hora de Ingreso |
| Q62 | - |  |  | SI | Información entregada por |
| Q63 | - |  |  | SI | Contacto |
| Q64 | - |  |  | SI | Fono Contacto |
| Q65 | - |  |  | SI | Procedencia del paciente |
| Q66 | - |  |  | SI | Procedencia, descripción |
| Q67 | - |  |  | SI | Comentarios y Observaciones |
| Q68 | - |  |  | SI | Toma de PKU |
| Q69 | - |  |  | SI | Profesional de Salud |
| Q70 | - |  |  | SI | Días gestación |
| Q71 | - |  |  | SI | + |
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