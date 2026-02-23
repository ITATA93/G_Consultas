# SQLUser.ARC_CashShiftCancReason

**Schema:** SQLUser
**Columnas:** 147
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CSCR_RowId | bigint | PK |  | NO | - |
| CQ22 | - |  |  | SI | (null) |
| CQ33 | - |  |  | SI | (null) |
| CQ34 | - |  |  | SI | (null) |
| CQ70 | - |  |  | SI | (null) |
| CQ74 | - |  |  | SI | (null) |
| CQ75 | - |  |  | SI | (null) |
| CQ76 | - |  |  | SI | (null) |
| CSCR_Code | varchar |  |  | NO | Code |
| CSCR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CSCR_CreatedDate | date |  |  | SI | Created Date |
| CSCR_CreatedTime | time |  |  | SI | Created Time |
| CSCR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CSCR_DateFrom | date |  |  | SI | Date From |
| CSCR_DateTo | date |  |  | SI | Date To |
| CSCR_Desc | varchar |  |  | NO | Description |
| CSCR_Owner | varchar |  |  | SI | Owner |
| CSCR_UpdatedDate | date |  |  | SI | Updated Date |
| CSCR_UpdatedTime | time |  |  | SI | Updated Time |
| CSCR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | ¿Consumo bebidas alcohólicas? |
| Q10 | - |  |  | SI | Circunferencia abdominal Mujer >= 88 cm. |
| Q11 | - |  |  | SI | Circunferencia abdominal Hombre >= 102 cm. |
| Q12 | - |  |  | SI | Presión arterial sistólica |
| Q12ObsDR | - |  |  | SI | Presión arterial sistólica DR |
| Q13 | - |  |  | SI | Presión arterial sistólica >= 140 mm/Hg |
| Q14 | - |  |  | SI | Presión arterial diastólica |
| Q14ObsDR | - |  |  | SI | Presión arterial diastólica DR |
| Q15 | - |  |  | SI | Presión arterial diastólica >= 90 mm/Hg |
| Q16 | - |  |  | SI | Glicemia en ayunas (mg/dl) |
| Q16ObsDR | - |  |  | SI | Glicemia en ayunas (mg/dl) DR |
| Q17 | - |  |  | SI | Glicemia en ayunas entre 100-125 mg/dl |
| Q18 | - |  |  | SI | Glicemia en ayunas >= 126 mg/dl |
| Q19 | - |  |  | SI | Hombres que tienen sexo con otros hombres, trabaja... |
| Q2 | - |  |  | SI | AUDIT Antíguo |
| Q20 | - |  |  | SI | VDRL |
| Q20ObsDR | - |  |  | SI | VDRL DR |
| Q21 | - |  |  | SI | RPR |
| Q21ObsDR | - |  |  | SI | RPR DR |
| Q22 | - |  |  | SI | ¿Ha tenido tos productiva por más de 15 días? |
| Q23 | - |  |  | SI | Fecha resultado PAP |
| Q24 | - |  |  | SI | PAP vigente |
| Q25 | - |  |  | SI | Resultado de PAP |
| Q25ObsDR | - |  |  | SI | Resultado de PAP DR |
| Q26 | - |  |  | SI | Resultado colesterol total |
| Q26ObsDR | - |  |  | SI | Resultado colesterol total DR |
| Q27 | - |  |  | SI | Colesterol total entre 200-239 mg/dl |
| Q28 | - |  |  | SI | Colesterol total >= 240 mg/dl |
| Q29 | - |  |  | SI | Mamografía realizada |
| Q2ObsDR | - |  |  | SI | AUDIT Antíguo DR |
| Q3 | - |  |  | SI | Tabaquismo |
| Q30 | - |  |  | SI | Resultado mamografía |
| Q30ObsDR | - |  |  | SI | Resultado mamografía DR |
| Q31 | - |  |  | SI | Debe generar Indicación de Baciloscopía |
| Q32 | - |  |  | SI | Fecha Vencimiento EMPA |
| Q33 | - |  |  | SI | Resultado Audit |
| Q34 | - |  |  | SI | Resultado Audit-C |
| Q35 | - |  |  | SI | Consejería según tipo de consumo |
| Q36 | - |  |  | SI | Consejería breve |
| Q37 | - |  |  | SI | Consejería en alimentación y actividad física |
| Q38 | - |  |  | SI | Fecha PAD |
| Q39 | - |  |  | SI | Refiere a perfil de Presión Arterial |
| Q4 | - |  |  | SI | Peso (kg.) |
| Q40 | - |  |  | SI | Refiere a PTGO |
| Q41 | - |  |  | SI | Referir a programa ITS |
| Q42 | - |  |  | SI | Baciloscopía |
| Q43 | - |  |  | SI | Fecha último Papanicolau |
| Q44 | - |  |  | SI | Resultado PAP |
| Q45 | - |  |  | SI | Toma de PAP |
| Q46 | - |  |  | SI | Refiere a consejería en alimentación saludable y a... |
| Q47 | - |  |  | SI | Refiere a confirmación Diagnóstica |
| Q48 | - |  |  | SI | Fecha última mamografía |
| Q49 | - |  |  | SI | Mamografía vigente |
| Q4ObsDR | - |  |  | SI | Peso (kg.) DR |
| Q5 | - |  |  | SI | Talla (cms.) |
| Q50 | - |  |  | SI | Mamografía alterada |
| Q51 | - |  |  | SI | Mamografía a otras edades realizada |
| Q52 | - |  |  | SI | Mamografía a otras edades alterada |
| Q53 | - |  |  | SI | Observaciones |
| Q54 | - |  |  | SI | Fecha ingreso observaciones |
| Q55 | - |  |  | SI | Fecha realización EMP |
| Q56 | - |  |  | SI | RUT |
| Q57 | - |  |  | SI | Profesional |
| Q58 | - |  |  | SI | Especialidad |
| Q59 | - |  |  | SI | Código Especialidad |
| Q5ObsDR | - |  |  | SI | Talla (cms.) DR |
| Q6 | - |  |  | SI | Índice de masa corporal (IMC) |
| Q60 | - |  |  | SI | Fecha registro resultado exámenes |
| Q61 | - |  |  | SI | Profesional |
| Q62 | - |  |  | SI | RUT |
| Q63 | - |  |  | SI | Especialidad |
| Q64 | - |  |  | SI | Código Especialidad |
| Q65 | - |  |  | SI | Fecha informa paciente |
| Q66 | - |  |  | SI | Profesional |
| Q67 | - |  |  | SI | RUT |
| Q68 | - |  |  | SI | Especialidad |
| Q69 | - |  |  | SI | Código Especialidad |
| Q7 | - |  |  | SI | Sobrepeso |
| Q70 | - |  |  | SI | Resultado CRAFFT |
| Q71 | - |  |  | SI | Refiere a confirmación diagnóstica |
| Q72 | - |  |  | SI | VDRL |
| Q73 | - |  |  | SI | RPR |
| Q74 | - |  |  | SI | Prueba ASSIST |
| Q75 | - |  |  | SI | Prueba CRAFFT |
| Q76 | - |  |  | SI | Prueba AUDIT |
| Q8 | - |  |  | SI | Obesidad |
| Q9 | - |  |  | SI | Circunferencia de cintura (cm.) |
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