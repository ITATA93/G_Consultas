# SQLUser.LBC_Antigen

**Schema:** SQLUser
**Columnas:** 180
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCAG_RowID | bigint | PK |  | NO | - |
| LBCAG_AdditionalBloodGroupSystem_DR | bigint |  | FK | SI | Additional Blood Group System Filter |
| LBCAG_Code | varchar |  |  | NO | Code
Collation exception to support k,K |
| LBCAG_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCAG_CreatedDate | date |  |  | SI | Created Date |
| LBCAG_CreatedTime | time |  |  | SI | Created Time |
| LBCAG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCAG_DateFrom | date |  |  | SI | Effective date for the record |
| LBCAG_DateTo | date |  |  | SI | Last day the record is active |
| LBCAG_Desc | varchar |  |  | NO | Description
Collation exception to support k,K
H... |
| LBCAG_Owner | varchar |  |  | SI | Owner |
| LBCAG_UpdatedDate | date |  |  | SI | Updated Date |
| LBCAG_UpdatedTime | time |  |  | SI | Updated Time |
| LBCAG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | COMPLICACIONES |
| Q02 | - |  |  | SI | ¿Ha presentado IAM? |
| Q03 | - |  |  | SI | Fecha IAM |
| Q04 | - |  |  | SI | ¿Ha Presentado AVE? |
| Q05 | - |  |  | SI | Fecha AVE |
| Q06 | - |  |  | SI | Clasificación de Wagner |
| Q07 | - |  |  | SI | ¿Ceguera por Diabetes? |
| Q08 | - |  |  | SI | Amputación Debida a DM |
| Q09 | - |  |  | SI | Observación de Amputaciones |
| Q10 | - |  |  | SI | ¿Retinopatía? |
| Q100 | - |  |  | SI | Temperatura Axilar |
| Q101 | - |  |  | SI | Pulso (Pulsos/Minutos) |
| Q102 | - |  |  | SI | Nefropatía Incipiente |
| Q103 | - |  |  | SI | Hematuria |
| Q104 | - |  |  | SI | Mantiene Resultado de Laboratorio |
| Q105 | - |  |  | SI | Método de cálculo |
| Q106 | - |  |  | SI | Otras alteraciones |
| Q107 | - |  |  | SI | OBS Otras alteraciones |
| Q108 | - |  |  | SI | Antecedentes Nefrouloroligos |
| Q109 | - |  |  | SI | Familiares 1er Grado con ERC |
| Q11 | - |  |  | SI | Fecha Retinopatía |
| Q110 | - |  |  | SI | Razón Albumina Creativita en Orina |
| Q111 | - |  |  | SI | Clasificación de ERC |
| Q112 | - |  |  | SI | Conducta a Seguir |
| Q113 | - |  |  | SI | Normal |
| Q114 | - |  |  | SI | Microalbuminuria |
| Q115 | - |  |  | SI | Macroalbuminuria |
| Q12 | - |  |  | SI | ¿Neuropatía? |
| Q13 | - |  |  | SI | Fecha Neuropatía |
| Q14 | - |  |  | SI | ¿Hipertrofia Ventricular Izquierda? |
| Q15 | - |  |  | SI | Fecha Hipertrofia Ventricular Izquierda |
| Q16 | - |  |  | SI | Cifras de presión elevadas en forma permanente: PA... |
| Q17 | - |  |  | SI | Presenta Obesidad |
| Q18 | - |  |  | SI | Pertenece a Grupo de Autoayuda |
| Q19 | - |  |  | SI | OTROS ANTECEDENTES |
| Q20 | - |  |  | SI | Antecedentes familiares de cardiopatía coronaria o... |
| Q21 | - |  |  | SI | Concentraciones elevadas de proteína C-rectiva, fi... |
| Q22 | - |  |  | SI | Microalbuminuria en diabéticos |
| Q23 | - |  |  | SI | Antecedentes personales de una enfermedad cardiova... |
| Q24 | - |  |  | SI | Concentración elevada de triglicéridos (>=150 mg/d... |
| Q25 | - |  |  | SI | Personas en tratamiento antihipertensivo (independ... |
| Q26 | - |  |  | SI | Personas con diabetes y nefropatía diabética estab... |
| Q27 | - |  |  | SI | HABITOS |
| Q28 | - |  |  | SI | ¿Usted Fuma? |
| Q29 | - |  |  | SI | ¿Sedentarismo? |
| Q30 | - |  |  | SI | ¿Adherencia a Dieta? |
| Q31 | - |  |  | SI | ¿Adherencia a Medicamentos? |
| Q32 | - |  |  | SI | Actividad Física |
| Q33 | - |  |  | SI | INGRESO CRÓNICO |
| Q34 | - |  |  | SI | ¿Es HTA? |
| Q35 | - |  |  | SI | Estado |
| Q36 | - |  |  | SI | ¿Es DM2? |
| Q37 | - |  |  | SI | Estado |
| Q38 | - |  |  | SI | ¿Tratamiento de Insulina? |
| Q39 | - |  |  | SI | ¿Es Dislipidémico? |
| Q40 | - |  |  | SI | Estado |
| Q41 | - |  |  | SI | EXAMENES |
| Q42 | - |  |  | SI | Fecha Realización Holter de Presión Arterial |
| Q43 | - |  |  | SI | Presión Arterial Holter |
| Q44 | - |  |  | SI | Observación Presión Arterial |
| Q45 | - |  |  | SI | Fondo de Ojos |
| Q46 | - |  |  | SI | Observación Fondo de Ojos |
| Q47 | - |  |  | SI | Fecha de Vigencia de fondo de Ojos |
| Q48 | - |  |  | SI | Ecocardiograma |
| Q49 | - |  |  | SI | Rx Torax |
| Q50 | - |  |  | SI | PTGO 120 min. |
| Q51 | - |  |  | SI | Fecha Vigencia PTGO |
| Q52 | - |  |  | SI | Hematocrito |
| Q53 | - |  |  | SI | Hemoglobina (Hb) |
| Q54 | - |  |  | SI | VHS (mm/hr) |
| Q55 | - |  |  | SI | Hemoglobina Glicosilada (HbA1c) |
| Q56 | - |  |  | SI | Hemoglucotest (mg/dl) |
| Q57 | - |  |  | SI | Glicemia (mg/dl) |
| Q58 | - |  |  | SI | Proteinuria (mg/día) |
| Q59 | - |  |  | SI | Microalbuminuria (mg7gr de creatininuria) |
| Q60 | - |  |  | SI | Clarence de Creatinina |
| Q61 | - |  |  | SI | Creatinina |
| Q62 | - |  |  | SI | Urea |
| Q63 | - |  |  | SI | N. Ureico |
| Q64 | - |  |  | SI | Acido Urico (mg/dl) |
| Q65 | - |  |  | SI | Orina Completa |
| Q66 | - |  |  | SI | Observación Orina Completa Alterada |
| Q67 | - |  |  | SI | VFG |
| Q68 | - |  |  | SI | Colesterol Total (mg/dl) |
| Q69 | - |  |  | SI | Colesterol HDL (mg/dl) |
| Q70 | - |  |  | SI | Triglicéridos (mg/dl) |
| Q71 | - |  |  | SI | Colesterol LDL (mg/dl) |
| Q72 | - |  |  | SI | Sodio |
| Q73 | - |  |  | SI | Potasio |
| Q74 | - |  |  | SI | Cloro |
| Q75 | - |  |  | SI | Edema |
| Q76 | - |  |  | SI | Observaciones |
| Q77 | - |  |  | SI | ELECTROCARDIOGRAMA |
| Q78 | - |  |  | SI | Fecha |
| Q79 | - |  |  | SI | Hora |
| Q80 | - |  |  | SI | Eléctrocardiograma |
| Q81 | - |  |  | SI | Resultado |
| Q82 | - |  |  | SI | Observaciones Eléctrocardiograma |
| Q83 | - |  |  | SI | Fecha Vigencia ECG |
| Q84 | - |  |  | SI | RC OLD |
| Q85 | - |  |  | SI | rc OLD2 |
| Q86 | - |  |  | SI | RCPF OLD3 |
| Q87 | - |  |  | SI | RF OLD4 |
| Q88 | - |  |  | SI | RCF OLD5 |
| Q89 | - |  |  | SI | Fecha Próximo Control |
| Q90 | - |  |  | SI | ANTECEDENTES VITALES |
| Q91 | - |  |  | SI | Peso (Kg) |
| Q92 | - |  |  | SI | Talla (Cm) |
| Q93 | - |  |  | SI | IMC |
| Q94 | - |  |  | SI | Estado Nutricional |
| Q95 | - |  |  | SI | Circunferencia de Cintura (Cm) |
| Q96 | - |  |  | SI | Circunferencia de Cadrera (Cm) |
| Q97 | - |  |  | SI | Indice Cintura de Cadera |
| Q98 | - |  |  | SI | PA Sistólica Sentado |
| Q99 | - |  |  | SI | PA Diastólica Sentado |
| QESTDIS | - |  |  | SI | Estado Dislipidemia |
| QESTDM2 | - |  |  | SI | Estado DM2 |
| QESTHTA | - |  |  | SI | Estado HTA |
| QOBSNEFRO | - |  |  | SI | Obs Antecedentes Nefrologicos |
| QPADDP | - |  |  | SI | PA Diastólica de Pie |
| QPASDP | - |  |  | SI | PA Sistólica de Pie |
| QPELG | - |  |  | SI | Personas  con una enfermedad lipídica genética |
| QPRCV | - |  |  | SI | Porcentaje de Riesgo Cardiovascular |
| QPTHTA | - |  |  | SI | Persona en Tratamiento Antihipertensivo (Independi... |
| QRCV | - |  |  | SI | Riesgo Cardiovascular |
| QSECVC | - |  |  | SI | Sin enf Cardiovascular pero con Col-total >280mg/d... |
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