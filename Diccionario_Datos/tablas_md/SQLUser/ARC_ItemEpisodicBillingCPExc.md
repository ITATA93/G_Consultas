# SQLUser.ARC_ItemEpisodicBillingCPExc

**Schema:** SQLUser
**Columnas:** 106
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CPEXC_ParRef | varchar | PK |  | NO | ARC_EpisodicBilling Parent Reference |
| CPEXC_AdmSource | varchar |  |  | SI | AdmSource |
| CPEXC_BillGrp | varchar |  |  | SI | ARCBillGrp |
| CPEXC_Childsub | double |  |  | NO | Childsub |
| CPEXC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CPEXC_CreatedDate | date |  |  | SI | Created Date |
| CPEXC_CreatedTime | time |  |  | SI | Created Time |
| CPEXC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CPEXC_DischDestin | varchar |  |  | SI | DischargeDestination |
| CPEXC_MaxAnaesthDays | double |  |  | SI | Maximum Anaesthetic Records  |
| CPEXC_MaxBillGrpDays | double |  |  | SI | Maximum Billing Group Days |
| CPEXC_MaxItemsAnaestTheatre | double |  |  | SI | Maximum Items per Anaesthetic/Theatre Record |
| CPEXC_MaxRoomTypeDays | double |  |  | SI | Maximum Room Type Days  |
| CPEXC_RevertPerDiemNoTheatre | varchar |  |  | SI | Revert to Per Diem if no Theatre |
| CPEXC_RoomType | varchar |  |  | SI | RoomType |
| CPEXC_RowId | varchar |  |  | NO | - |
| CPEXC_UpdatedDate | date |  |  | SI | Updated Date |
| CPEXC_UpdatedTime | time |  |  | SI | Updated Time |
| CPEXC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha Evaluación |
| Q02 | - |  |  | SI | Hora Evaluación |
| Q03 | - |  |  | SI | Responsable Evaluación |
| Q04 | - |  |  | SI | ADDENBROOKE’S COGNITIVE EXAMINATION – ACE-III   Ve... |
| Q05 | - |  |  | SI | ATENCION |
| Q06 | - |  |  | SI | Pregunte: ¿En que…estamos? |
| Q07 | - |  |  | SI | Pregunte: ¿En que…estamos? |
| Q08 | - |  |  | SI | Diga: “Le voy a decir 3 palabras y me gustaría que... |
| Q09 | - |  |  | SI | Registro número de ensayo |
| Q10 | - |  |  | SI | ¿Ahora por favor dígame cuánto es 100 menos 7?  … ... |
| Q11 | - |  |  | SI | MEMORIA |
| Q12 | - |  |  | SI | Diga: “¿Cuáles eran las 3 palabras que yo le pedí ... |
| Q13 | - |  |  | SI | FLUENCIA (CONTESTAR RECUEADRO PRINCIPIO PÁGINA) |
| Q14 | - |  |  | SI | Letras: Le voy a pedir que durante un minuto me di... |
| Q15 | - |  |  | SI | Cuantas palabra pudo decir ? |
| Q16 | - |  |  | SI | Animales: Diga: “¿Ahora dígame todos los animales ... |
| Q17 | - |  |  | SI | Cuantos Animales pudo decir ? |
| Q18 | - |  |  | SI | Diga: “Voy a decirle un nombre y una dirección y m... |
| Q19 | - |  |  | SI | Primer Ensayo |
| Q20 | - |  |  | SI | Segundo Ensayo |
| Q21 | - |  |  | SI | Tercer Ensayo (Valido) |
| Q22 | - |  |  | SI | Cual es el Nombre? |
| Q23 | - |  |  | SI | LENGUAJE |
| Q24 | - |  |  | SI | Ahora le voy a dar algunas instrucciones simples. |
| Q25 | - |  |  | SI | Diga al sujeto |
| Q26 | - |  |  | SI | Diga: “Me gustaría que escriba dos oraciones. Pued... |
| Q27 | - |  |  | SI | Por favor repita: ‘hipopótamo’,  ‘excentricidad’, ... |
| Q28 | - |  |  | SI | Por favor repita: ‘El flan tiene frutillas y framb... |
| Q29 | - |  |  | SI | Ahora repita: “La orquesta tocó y la audiencia apl... |
| Q30 | - |  |  | SI | Por favor lea en voz alta las siguientes palabras ... |
| Q31 | - |  |  | SI | Diagrama de Infinidad: Por favor copie este dibujo... |
| Q32 | - |  |  | SI | Cubo: Por favor copie este dibujo |
| Q33 | - |  |  | SI | Pida al examinado que nombre las siguientes imagen... |
| Q34 | - |  |  | SI | Usando las imágenes que aparecen anteriormente, pi... |
| Q35 | - |  |  | SI | HABILIDADES VISOESPACIALES |
| Q36 | - |  |  | SI | Reloj: Por favor dibuje un reloj, con todos los nú... |
| Q37 | - |  |  | SI | Por favor cuente los puntos en cada cuadrado sin s... |
| Q38 | - |  |  | SI | Por favor dígame que letras son estas (Puntaje) |
| Q39 | - |  |  | SI | Diga: “Ahora dígame, por favor, lo que usted recue... |
| Q40 | - |  |  | SI | Sub-prueba de Memoria |
| Q41 | - |  |  | SI | PUNTAJE TOTAL ACE-III |
| Q42 | - |  |  | SI | Atención |
| Q43 | - |  |  | SI | Memoria |
| Q44 | - |  |  | SI | Fluencia |
| Q45 | - |  |  | SI | Lenguaje |
| Q46 | - |  |  | SI | Visoespacial |
| Q47 | - |  |  | SI | PUNTAJE TOTAL M-ACE |
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