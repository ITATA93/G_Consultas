# SQLUser.LBC_QCSchemeType

**Schema:** SQLUser
**Columnas:** 112
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCQCST_RowID | bigint | PK |  | NO | - |
| ChildQ160DR | - |  |  | SI | Child Reference: Dispositivos |
| LBCQCST_Code | varchar |  |  | SI | Code |
| LBCQCST_CreatedDate | date |  |  | SI | Created Date |
| LBCQCST_CreatedTime | time |  |  | SI | Created Time |
| LBCQCST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCQCST_Desc | varchar |  |  | SI | Description |
| LBCQCST_UpdatedDate | date |  |  | SI | Updated Date |
| LBCQCST_UpdatedTime | time |  |  | SI | Updated Time |
| LBCQCST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q0141 | - |  |  | SI | Otro |
| Q0242 | - |  |  | SI | Otro |
| Q0243 | - |  |  | SI | Otros |
| Q0344 | - |  |  | SI | Comentarios |
| Q0445 | - |  |  | SI | Otro |
| Q0446 | - |  |  | SI | Otros |
| Q0547 | - |  |  | SI | Otro |
| Q0548 | - |  |  | SI | Otro |
| Q060 | - |  |  | SI | Comentario Medicamentos |
| Q0750 | - |  |  | SI | Comentarios |
| Q10 | - |  |  | SI | Posición del Paciente |
| Q11 | - |  |  | SI | Dispositivos para Posición |
| Q12 | - |  |  | SI | Prevención de UPP |
| Q13 | - |  |  | SI | Otras |
| Q14 | - |  |  | SI | Puntos de Apoyo Protegidos |
| Q15 | - |  |  | SI | Otro |
| Q16 | - |  |  | SI | Prevención TVP |
| Q17 | - |  |  | SI | Otro |
| Q18 | - |  |  | SI | Item |
| Q19 | - |  |  | SI | Otro |
| Q20 | - |  |  | SI | Descripción de Item |
| Q21 | - |  |  | SI | Fecha de Vencimiento |
| Q22 | - |  |  | SI | Control de Viraje |
| Q23 | - |  |  | SI | APÓSITOS Y VENDAJES |
| Q24 | - |  |  | SI | Herida Operatoria (Ejemplo: Abdomen) |
| Q25 | - |  |  | SI | Tipo Apósito/Vendaje |
| Q26 | - |  |  | SI | Condición Apósito/Vendaje |
| Q27 | - |  |  | SI | CAUTERIZACIÓN |
| Q28 | - |  |  | SI | Tipo de Generador Electroquirúrgico |
| Q29 | - |  |  | SI | Energía Utilizada |
| Q30 | - |  |  | SI | Localización de Placa Electrobisturí |
| Q31 | - |  |  | SI | Responsable de la Colocación Electrobisturí |
| Q32 | - |  |  | SI | RECUENTO INCORRECTO |
| Q33 | - |  |  | SI | Items Recuento Incorrecto |
| Q34 | - |  |  | SI | Acción Recuento Incorrecto |
| Q35 | - |  |  | SI | USO DE IRRIGACIÓN |
| Q36 | - |  |  | SI | Solución de Irrigación |
| Q37 | - |  |  | SI | Otro |
| Q38 | - |  |  | SI | Volumen Total de Entrada (ML) |
| Q39 | - |  |  | SI | Volumen Total de Salida (ML) |
| Q40 | - |  |  | SI | Medicamentos |
| Q49 | - |  |  | SI | Responsable del Recuento |
| Q52 | - |  |  | SI | Tipo de Láser |
| Q53 | - |  |  | SI | Modo de Láser |
| Q54 | - |  |  | SI | Otro |
| Q55 | - |  |  | SI | Refigerante Utilizado |
| Q56 | - |  |  | SI | Potencia |
| Q57 | - |  |  | SI | Total Uso de Láser |
| Q58 | - |  |  | SI | Seguridad Láser |
| Q59 | - |  |  | SI | Otro |
| Q60 | - |  |  | SI | Ubicación Mango Isquemia |
| Q61 | - |  |  | SI | 2. Posición del Paciente |
| Q62 | - |  |  | SI | Dispositivos para Posición |
| Q63 | - |  |  | SI | Profilaxis Mecánica |
| Q64 | - |  |  | SI | Profilaxis Farmacológica |
| Q65 | - |  |  | SI | No Aplica (TVP) |
| Q66 | - |  |  | SI | Observaciones (TVP) |
| Q67 | - |  |  | SI | Responsable Operador Monitor Electrobisturí |
| Q68 | - |  |  | SI | Nombre del Cirujano que se Notifico |
| Q69 | - |  |  | SI | Otros |
| Q70 | - |  |  | SI | Nombre de los Medicamentos |
| Q71 | - |  |  | SI | Cierre de Herida Operatoria |
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