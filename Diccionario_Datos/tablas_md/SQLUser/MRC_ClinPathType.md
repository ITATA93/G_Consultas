# SQLUser.MRC_ClinPathType

**Schema:** SQLUser
**Columnas:** 249
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CLPT_RowId | bigint | PK |  | NO | - |
| CLPT_Code | varchar |  |  | NO | Code |
| CLPT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CLPT_CreatedDate | date |  |  | SI | Created Date |
| CLPT_CreatedTime | time |  |  | SI | Created Time |
| CLPT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CLPT_Desc | varchar |  |  | NO | Description |
| CLPT_OrderingWorkFlow_DR | bigint |  | FK | SI | Ordering Workflow |
| CLPT_Owner | varchar |  |  | SI | Owner |
| CLPT_UpdatedDate | date |  |  | SI | Updated Date |
| CLPT_UpdatedTime | time |  |  | SI | Updated Time |
| CLPT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CQ159 | - |  |  | SI | (null) |
| CQ27 | - |  |  | SI | (null) |
| CQ30 | - |  |  | SI | (null) |
| CQ37 | - |  |  | SI | (null) |
| CQ51 | - |  |  | SI | (null) |
| CQ52 | - |  |  | SI | (null) |
| CQ55 | - |  |  | SI | (null) |
| CQ75 | - |  |  | SI | (null) |
| CQ93 | - |  |  | SI | (null) |
| CQregla | - |  |  | SI | (null) |
| ChildQ160DR | - |  |  | SI | Child Reference: Lactancia |
| Q1 | - |  |  | SI | Peso(kg) |
| Q10 | - |  |  | SI | ¿Realiza actividad fisica? |
| Q100 | - |  |  | SI | Alergia al espermicida |
| Q101 | - |  |  | SI | Cáncer cérvico-uterino |
| Q102 | - |  |  | SI | Cáncer de la mama |
| Q103 | - |  |  | SI | Complicaciones del embarazo con DIU |
| Q104 | - |  |  | SI | Enfermedad inflamatoria pélvica aguda |
| Q105 | - |  |  | SI | Enfermedad tromboembólica |
| Q106 | - |  |  | SI | Enfermedades hepáticas |
| Q107 | - |  |  | SI | Hipertensión arterial |
| Q108 | - |  |  | SI | Infarto del miocardio |
| Q109 | - |  |  | SI | Patología cardiovascular arterial |
| Q11 | - |  |  | SI | Edad inicio de actividad sexual (años) |
| Q110 | - |  |  | SI | Perforación |
| Q111 | - |  |  | SI | Alergia al látex |
| Q112 | - |  |  | SI | Alteraciones del sangrado uterino |
| Q113 | - |  |  | SI | Ánimo depresivo |
| Q114 | - |  |  | SI | Aumento de peso |
| Q115 | - |  |  | SI | Cansancio |
| Q116 | - |  |  | SI | Cefalea |
| Q117 | - |  |  | SI | Cloasma |
| Q118 | - |  |  | SI | Disminucion de la libido |
| Q119 | - |  |  | SI | Dolor |
| Q12 | - |  |  | SI | Clasificación de dependencia |
| Q120 | - |  |  | SI | Dolor durante el coito |
| Q121 | - |  |  | SI | Edema |
| Q122 | - |  |  | SI | Flujo vaginal inespecífico |
| Q123 | - |  |  | SI | Folículos persistentes o quistes foliculares |
| Q124 | - |  |  | SI | Incrustación |
| Q125 | - |  |  | SI | Infección |
| Q126 | - |  |  | SI | Irritabilidad |
| Q127 | - |  |  | SI | Mastalgia |
| Q128 | - |  |  | SI | Náuseas |
| Q129 | - |  |  | SI | Sangrado o goteo irregular (spotting) |
| Q12ObsDR | - |  |  | SI | Clasificación de dependencia DR |
| Q13 | - |  |  | SI | Edad menarquia |
| Q130 | - |  |  | SI | Sensibilidad en las mamas |
| Q131 | - |  |  | SI | Tensión premenstrual |
| Q132 | - |  |  | SI | Vómitos |
| Q133 | - |  |  | SI | Accidente vascular cerebral |
| Q134 | - |  |  | SI | Cambios metabólicos |
| Q135 | - |  |  | SI | Clasificación circunferencia de la cintura |
| Q135ObsDR | - |  |  | SI | Clasificación circunferencia de la cintura DR |
| Q136 | - |  |  | SI | Puntaje |
| Q137 | - |  |  | SI | Piezas dentales presentes |
| Q139 | - |  |  | SI | ¿Se le entrego la  guía para la gestación y el nac... |
| Q14 | - |  |  | SI | Edad de la menopausia |
| Q140 | - |  |  | SI | Resultado Riesgo Psicosocial Abreviado |
| Q140ObsDR | - |  |  | SI | Resultado Riesgo Psicosocial Abreviado DR |
| Q141 | - |  |  | SI | ¿Presenta algún riesgo psicosocial de acuerdo a la... |
| Q142 | - |  |  | SI | 1 |
| Q143 | - |  |  | SI | ¿Existe alguna situación de vulnerablidad social d... |
| Q144 | - |  |  | SI | 2 |
| Q145 | - |  |  | SI | ¿Está de acuerdo con integrarse a visitas dimicili... |
| Q146 | - |  |  | SI | Fisiológico |
| Q147 | - |  |  | SI | De alto riesgo |
| Q148 | - |  |  | SI | Continúa control ARO en |
| Q149 | - |  |  | SI | ¿Quién la acompaña en el control ? |
| Q15 | - |  |  | SI | Edad espermarca (años) |
| Q150 | - |  |  | SI | Acude sola al control |
| Q151 | - |  |  | SI | Conyuge o pareja |
| Q152 | - |  |  | SI | Madre de la gestante |
| Q153 | - |  |  | SI | Otro (especificar parentesco o relación con la ges... |
| Q156 | - |  |  | SI | Circunferencia Abdominal |
| Q156ObsDR | - |  |  | SI | Circunferencia Abdominal DR |
| Q157 | - |  |  | SI | Resultado de Escala de Edimburgo |
| Q158 | - |  |  | SI | Método Anticonceptivo Preferido |
| Q158ObsDR | - |  |  | SI | Método Anticonceptivo Preferido DR |
| Q159 | - |  |  | SI | Lactancia |
| Q16 | - |  |  | SI | En el inicio de su vida sexual ¿usó preservativo? |
| Q17 | - |  |  | SI | ¿Activo sexualmente? |
| Q18 | - |  |  | SI | ¿Cómo percibe su vida sexual actualmente? |
| Q19 | - |  |  | SI | Nº de parejas sexuales |
| Q1ObsDR | - |  |  | SI | Peso(kg) DR |
| Q2 | - |  |  | SI | Talla (cms.) |
| Q20 | - |  |  | SI | ¿En los últimos 12 meses usó preservativo? |
| Q21 | - |  |  | SI | Fecha último embarazo |
| Q22 | - |  |  | SI | N° de gestas |
| Q23 | - |  |  | SI | N° de hijos vivos |
| Q24 | - |  |  | SI | N° de abortos |
| Q25 | - |  |  | SI | Rersultado examen físico de mamas |
| Q25ObsDR | - |  |  | SI | Rersultado examen físico de mamas DR |
| Q26 | - |  |  | SI | Fecha resultado PAP |
| Q27 | - |  |  | SI | Resultado PAP |
| Q28 | - |  |  | SI | Fecha resultado flujo vaginal |
| Q29 | - |  |  | SI | Resultado flujo vaginal |
| Q29ObsDR | - |  |  | SI | Resultado flujo vaginal DR |
| Q2ObsDR | - |  |  | SI | Talla (cms.) DR |
| Q3 | - |  |  | SI | Índice de masa corporal (IMC) |
| Q30 | - |  |  | SI | Método anticonceptivo |
| Q31 | - |  |  | SI | Fecha inicio método anticonceptivo principal |
| Q32 | - |  |  | SI | ¿Efectos adversos? |
| Q34 | - |  |  | SI | Observacion de otros efectos adversos |
| Q35 | - |  |  | SI | ¿Se encuentra con terapia hormonal de reemplazo? |
| Q36 | - |  |  | SI | Fecha inicio terapia hormonal de reemplazo |
| Q37 | - |  |  | SI | ¿Qué método anticonceptivo utiliza con su pareja? |
| Q38 | - |  |  | SI | Clasificación presión arterial |
| Q39 | - |  |  | SI | Clasificacion glicemia venosa en ayunas |
| Q4 | - |  |  | SI | Calificación estado nutricional según IMC |
| Q40 | - |  |  | SI | Clasificacion sobrecarga de glucosa |
| Q41 | - |  |  | SI | ¿Se aplicó QUALIDIAB? |
| Q42 | - |  |  | SI | Fecha aplicación QUALIDIAB |
| Q43 | - |  |  | SI | ¿Se encuentra con tratamiento de insulina? |
| Q44 | - |  |  | SI | ¿Tiene úlcera activa en pie? |
| Q45 | - |  |  | SI | ¿Tiene úlcera activa tratada con manejo avanzado d... |
| Q46 | - |  |  | SI | ¿Amputación de pie debida a DM? |
| Q47 | - |  |  | SI | Grupo de Riesgo Ulceración |
| Q47ObsDR | - |  |  | SI | Grupo de Riesgo Ulceración DR |
| Q48 | - |  |  | SI | Clasificación Colesterol |
| Q49 | - |  |  | SI | ¿Completó el módulo de actividad física? |
| Q4ObsDR | - |  |  | SI | Calificación estado nutricional según IMC DR |
| Q5 | - |  |  | SI | Circunferencia de cintura (cm.) |
| Q50 | - |  |  | SI | Resultado evaluación de riesgo suicida (OKASHA) |
| Q50ObsDR | - |  |  | SI | Resultado evaluación de riesgo suicida (OKASHA) DR |
| Q51 | - |  |  | SI | Clasificación discapacidad de causa psíquica |
| Q52 | - |  |  | SI | Resultado atención de salud mental |
| Q53 | - |  |  | SI | Resultado AUDIT |
| Q53ObsDR | - |  |  | SI | Resultado AUDIT DR |
| Q54 | - |  |  | SI | Clasificación consumo de sustancias ilícitas |
| Q55 | - |  |  | SI | Resultado atención odontológica |
| Q56 | - |  |  | SI | Índice COP |
| Q57 | - |  |  | SI | Cariadas - N° sextante I |
| Q58 | - |  |  | SI | Cariadas - N° sextante II |
| Q59 | - |  |  | SI | Cariadas - N° sextante III |
| Q6 | - |  |  | SI | Diagnóstico nutricional |
| Q60 | - |  |  | SI | Cariadas - N° sextante IV |
| Q61 | - |  |  | SI | Cariadas - N° sextante V |
| Q62 | - |  |  | SI | Cariadas - N° sextante VI |
| Q63 | - |  |  | SI | Obturadas - N° sextante I |
| Q64 | - |  |  | SI | Obturadas - N° sextante II |
| Q65 | - |  |  | SI | Obturadas - N° sextante III |
| Q66 | - |  |  | SI | Obturadas - N° sextante IV |
| Q67 | - |  |  | SI | Obturadas - N° sextante V |
| Q68 | - |  |  | SI | Obturadas - N° sextante VI |
| Q69 | - |  |  | SI | Perdidas - N° sextante I |
| Q6ObsDR | - |  |  | SI | Diagnóstico nutricional DR |
| Q7 | - |  |  | SI | Presión Arterial Sistólica |
| Q70 | - |  |  | SI | Perdidas - N° sextante II |
| Q71 | - |  |  | SI | Perdidas - N° sextante III |
| Q72 | - |  |  | SI | Perdidas - N° sextante IV |
| Q73 | - |  |  | SI | Perdidas - N° sextante V |
| Q74 | - |  |  | SI | Perdidas - N° sextante VI |
| Q75 | - |  |  | SI | Derivacion a red asistencial |
| Q76 | - |  |  | SI | Fecha resultado glicemia venosa en ayunas |
| Q77 | - |  |  | SI | Resultado glicemia venosa en ayunas |
| Q77ObsDR | - |  |  | SI | Resultado glicemia venosa en ayunas DR |
| Q78 | - |  |  | SI | Fecha resultado prueba sobrecarga a la glucosa |
| Q79 | - |  |  | SI | Resultado prueba de sobrecarga a la glucosa |
| Q7ObsDR | - |  |  | SI | Presión Arterial Sistólica DR |
| Q8 | - |  |  | SI | Riesgo Cardiovascular |
| Q80 | - |  |  | SI | Fecha hemoglobina glicosilada |
| Q81 | - |  |  | SI | Resultado hemoglobina glicosilada |
| Q81ObsDR | - |  |  | SI | Resultado hemoglobina glicosilada DR |
| Q82 | - |  |  | SI | Fecha resultado colesterol total |
| Q83 | - |  |  | SI | Resultado colesterol total |
| Q83ObsDR | - |  |  | SI | Resultado colesterol total DR |
| Q84 | - |  |  | SI | Fecha resultado VDRL |
| Q85 | - |  |  | SI | Resultado VDRL |
| Q85ObsDR | - |  |  | SI | Resultado VDRL DR |
| Q86 | - |  |  | SI | Fecha resultado RPR |
| Q87 | - |  |  | SI | Resultado RPR |
| Q87ObsDR | - |  |  | SI | Resultado RPR DR |
| Q88 | - |  |  | SI | Fecha resultado test de ELISA |
| Q89 | - |  |  | SI | Resultado test de ELISA |
| Q89ObsDR | - |  |  | SI | Resultado test de ELISA DR |
| Q8ObsDR | - |  |  | SI | Riesgo Cardiovascular DR |
| Q9 | - |  |  | SI | Tabaquismo |
| Q90 | - |  |  | SI | Fecha resultado baciloscopía |
| Q91 | - |  |  | SI | Resultado baciloscopía |
| Q91ObsDR | - |  |  | SI | Resultado baciloscopía DR |
| Q92 | - |  |  | SI | Fecha resultado antígeno prostático |
| Q93 | - |  |  | SI | Resultado antígeno prostático |
| Q94 | - |  |  | SI | Fecha resultado mamografía |
| Q95 | - |  |  | SI | Resultado mamografía |
| Q95ObsDR | - |  |  | SI | Resultado mamografía DR |
| Q96 | - |  |  | SI | Fecha ecografía mamaria |
| Q97 | - |  |  | SI | Resultado ecografía mamaria |
| Q97ObsDR | - |  |  | SI | Resultado ecografía mamaria DR |
| Q98 | - |  |  | SI | Indicar efecto(s) adverso(s): |
| Q99 | - |  |  | SI | Acné |
| QMIM2 | - |  |  | SI | Mujer con Infante Menor de 2 Años |
| QMIM2ObsDR | - |  |  | SI | Mujer con Infante Menor de 2 Años DR |
| QMPP | - |  |  | SI | Meses Post-Parto |
| QPAD | - |  |  | SI | Presión arterial diastólica (mmHg) |
| QPADObsDR | - |  |  | SI | Presión arterial diastólica (mmHg) DR |
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
| Qregla | - |  |  | SI | regla |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*