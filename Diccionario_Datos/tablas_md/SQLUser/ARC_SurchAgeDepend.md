# SQLUser.ARC_SurchAgeDepend

**Schema:** SQLUser
**Columnas:** 272
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AGE_ParRef | bigint | PK |  | NO | ARC_SurchargeCode Parent Reference |
| AGE_Childsub | double |  |  | NO | Childsub |
| AGE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| AGE_CreatedDate | date |  |  | SI | Created Date |
| AGE_CreatedTime | time |  |  | SI | Created Time |
| AGE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AGE_DateFrom | date |  |  | SI | Date From |
| AGE_DateTo | date |  |  | SI | Date To |
| AGE_DayFrom | double |  |  | SI | Day From |
| AGE_DayTo | double |  |  | SI | Day To |
| AGE_FixedAmt | double |  |  | SI | Fixed Amt |
| AGE_Name | varchar |  |  | SI | Description |
| AGE_Perc | double |  |  | SI | % Charge |
| AGE_RowId | varchar |  |  | NO | - |
| AGE_UpdatedDate | date |  |  | SI | Updated Date |
| AGE_UpdatedTime | time |  |  | SI | Updated Time |
| AGE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| AGE_VisitType | varchar |  |  | SI | Visit Type |
| AGE_YearFrom | double |  |  | SI | Year From |
| AGE_YearTo | double |  |  | SI | Year To |
| ChildQ09DR | - |  |  | SI | Child Reference: Motivo de consulta según acompaña... |
| Q01 | - |  |  | SI | Control en Establecimiento |
| Q02 | - |  |  | SI | Establecimiento Educacional |
| Q03 | - |  |  | SI | Beneficiario Protección Social |
| Q04 | - |  |  | SI | País de Origen |
| Q05 | - |  |  | SI | Estado Civil |
| Q06 | - |  |  | SI | Pueblo Indígena |
| Q07 | - |  |  | SI | Acompañante |
| Q10 | - |  |  | SI | Descripción motivo de consulta |
| Q100 | - |  |  | SI | Edad Menarca / espermarca (años) |
| Q101 | - |  |  | SI | Edad Menarca / espermarca (meses) |
| Q102 | - |  |  | SI | Fecha de última menstruación |
| Q103 | - |  |  | SI | Fecha ultima menstruación desconocida |
| Q104 | - |  |  | SI | Ciclos regulares |
| Q105 | - |  |  | SI | Dismenorrea |
| Q106 | - |  |  | SI | Flujo patológico vaginal / secreción peneana |
| Q107 | - |  |  | SI | ITS / VIH |
| Q108 | - |  |  | SI | Especificar enfermedad de transmisión sexual |
| Q109 | - |  |  | SI | Tratamiento ITS/VIH |
| Q11 | - |  |  | SI | Perinatales normales |
| Q110 | - |  |  | SI | Tratamiento ITS/VIH de contactos |
| Q111 | - |  |  | SI | Embarazos |
| Q112 | - |  |  | SI | Hijos |
| Q113 | - |  |  | SI | Abortos |
| Q114 | - |  |  | SI | Observaciones (Gineco-Urológico) |
| Q115 | - |  |  | SI | Orientación sexual |
| Q116 | - |  |  | SI | Se identifica como: |
| Q117 | - |  |  | SI | Intención o conducta sexual |
| Q118 | - |  |  | SI | Edad de inicio intención o conducta sexual |
| Q119 | - |  |  | SI | Relaciones sexuales con |
| Q12 | - |  |  | SI | Alergias |
| Q120 | - |  |  | SI | Pareja sexual |
| Q121 | - |  |  | SI | Dificultades en relaciones sexuales |
| Q122 | - |  |  | SI | ¿Uso habitual del condón? |
| Q123 | - |  |  | SI | Doble protección |
| Q124 | - |  |  | SI | Uso MAC actual |
| Q125 | - |  |  | SI | Especificar cual MAC? |
| Q126 | - |  |  | SI | Razón no uso MAC |
| Q127 | - |  |  | SI | Consejería uso MAC |
| Q128 | - |  |  | SI | ACO de emergencia |
| Q129 | - |  |  | SI | Violencia sexual |
| Q13 | - |  |  | SI | Vacunas completas |
| Q130 | - |  |  | SI | ¿Ha existido reparación? |
| Q131 | - |  |  | SI | Observaciones (Sexualidad) |
| Q132 | - |  |  | SI | Imagen corporal |
| Q133 | - |  |  | SI | Vida con proyecto |
| Q134 | - |  |  | SI | Bienestar emocional |
| Q135 | - |  |  | SI | Suicidio amigo/a o familiar cercano |
| Q136 | - |  |  | SI | Ideación suicida (último mes) |
| Q137 | - |  |  | SI | Intento suicida (últimos 3 meses) |
| Q138 | - |  |  | SI | Referente adulto |
| Q139 | - |  |  | SI | Nombre Referente |
| Q14 | - |  |  | SI | Enf. Importantes (Personales) |
| Q140 | - |  |  | SI | Teléfono referente |
| Q141 | - |  |  | SI | Observaciones (Situación Psicoemocional) |
| Q142 | - |  |  | SI | Peso (Kg) |
| Q142ObsDR | - |  |  | SI | Peso (Kg) DR |
| Q143 | - |  |  | SI | Talla (cm) |
| Q143ObsDR | - |  |  | SI | Talla (cm) DR |
| Q144 | - |  |  | SI | Desviación estándar  (Talla) |
| Q145 | - |  |  | SI | Perímetro Cintura (cm) |
| Q145ObsDR | - |  |  | SI | Perímetro Cintura (cm) DR |
| Q146 | - |  |  | SI | IMC |
| Q147 | - |  |  | SI | DE (IMC) |
| Q148 | - |  |  | SI | Presión arterial sistólica |
| Q148ObsDR | - |  |  | SI | Presión arterial sistólica DR |
| Q149 | - |  |  | SI | Presión arterial diastólica |
| Q149ObsDR | - |  |  | SI | Presión arterial diastólica DR |
| Q15 | - |  |  | SI | Discapacidad |
| Q150 | - |  |  | SI | Tanner mama |
| Q150ObsDR | - |  |  | SI | Tanner mama DR |
| Q151 | - |  |  | SI | Tanner genital |
| Q151ObsDR | - |  |  | SI | Tanner genital DR |
| Q152 | - |  |  | SI | Con foto |
| Q153 | - |  |  | SI | Aspecto general |
| Q154 | - |  |  | SI | Agudeza visual |
| Q155 | - |  |  | SI | Agudeza auditiva |
| Q156 | - |  |  | SI | Salud bucal |
| Q157 | - |  |  | SI | Tiroides |
| Q158 | - |  |  | SI | Cardiopulmonar |
| Q159 | - |  |  | SI | Abdomen |
| Q16 | - |  |  | SI | Accidente relevante |
| Q160 | - |  |  | SI | Columna |
| Q161 | - |  |  | SI | Extremidades |
| Q162 | - |  |  | SI | Observaciones (Examen Físico) |
| Q163 | - |  |  | SI | Detección de Riesgo |
| Q164 | - |  |  | SI | Otro riesgo |
| Q165 | - |  |  | SI | Impresión Diagnóstica Integral (No diagnósticos) |
| Q166 | - |  |  | SI | Fecha Próxima Visita |
| Q167 | - |  |  | SI | Alertas Antecedentes Personales |
| Q168 | - |  |  | SI | Alertas Antecedentes Familiares |
| Q169 | - |  |  | SI | Alertas Educación |
| Q17 | - |  |  | SI | Cirugía / hospializaciones |
| Q170 | - |  |  | SI | Alertas Trabajo |
| Q171 | - |  |  | SI | Alertas Vida Social |
| Q172 | - |  |  | SI | Alertas Hábitos / Consumo |
| Q173 | - |  |  | SI | Alertas Gineco-Urológicas |
| Q174 | - |  |  | SI | Alertas Sexualidad |
| Q175 | - |  |  | SI | Alertas Situación Psicoemocional |
| Q176 | - |  |  | SI | Alertas Examen Físico |
| Q177 | - |  |  | SI | Alertas de Detección de Riesgos |
| Q178 | - |  |  | SI | Vive Con |
| Q179 | - |  |  | SI | Nivel de Instrucción de la Familia |
| Q18 | - |  |  | SI | Uso medicamentos |
| Q180 | - |  |  | SI | Detección Riesgo |
| Q181 | - |  |  | SI | Indicaciones e Interconsultas |
| Q182 | - |  |  | SI | Nombrar Institución |
| Q183 | - |  |  | SI | Modalidad de Estudio |
| Q184 | - |  |  | SI | Clases Virtuales (Horas al día) |
| Q185 | - |  |  | SI | Exposición a Pantallas (Horas al día) |
| Q186 | - |  |  | SI | Acceso a redes sociales y plataformas virtuales |
| Q187 | - |  |  | SI | Violencia Virtual |
| Q188 | - |  |  | SI | Alimentación Inadecuada |
| Q189 | - |  |  | SI | ¿Ya tuvo la menarquia o espermarquia? |
| Q19 | - |  |  | SI | Problemas salud mental |
| Q190 | - |  |  | SI | Ritmo menstrual Duración (días menstruación):N/S-N... |
| Q191 | - |  |  | SI | Ritmo menstrual: Periodicidad (intervalos):N/S-N/C |
| Q192 | - |  |  | SI | ¿Ha tenido relaciones sexuales? |
| Q193 | - |  |  | SI | ¿Pareja sexual? |
| Q194 | - |  |  | SI | ¿Edad pareja? |
| Q195 | - |  |  | SI | ¿Edad inicio relaciones sexuales? |
| Q196 | - |  |  | SI | ¿Tipo practica sexual? |
| Q197 | - |  |  | SI | ¿Ha tenido episodios de violencia física, en su re... |
| Q198 | - |  |  | SI | ¿Ha tenido episodios de violencia sexual, en su re... |
| Q199 | - |  |  | SI | ¿Ha tenido episodios de violencia psicológica, en ... |
| Q20 | - |  |  | SI | Violencia |
| Q200 | - |  |  | SI | ¿Antecedente de IVE? |
| Q201 | - |  |  | SI | ¿Estado de ánimo en el último mes? |
| Q202 | - |  |  | SI | ¿Deseo de estar muerto en el último mes? |
| Q203 | - |  |  | SI | Correo electrónico |
| Q204 | - |  |  | SI | Desviación estándar (Peso) |
| Q205 | - |  |  | SI | Desviación estándar (Perímetro Cintura) |
| Q206 | - |  |  | SI | Presión Arterial |
| Q21 | - |  |  | SI | Judiciales (Personales) |
| Q22 | - |  |  | SI | Otros (Personales) |
| Q23 | - |  |  | SI | Observaciones (Antecedentes Personales) |
| Q24 | - |  |  | SI | Enf. Importantes (Familiares) |
| Q25 | - |  |  | SI | Obesidad |
| Q26 | - |  |  | SI | Problemas salud mental (Familiar) |
| Q27 | - |  |  | SI | Violencia intrafamiliar |
| Q28 | - |  |  | SI | Alcohol y otras drogas |
| Q29 | - |  |  | SI | Madre y/o padre adolescente |
| Q30 | - |  |  | SI | Judiciales (Familiares) |
| Q31 | - |  |  | SI | Otros (Familiares) |
| Q32 | - |  |  | SI | Observaciones (Antecedentes Familiares) |
| Q33 | - |  |  | SI | Vive Solo/a |
| Q34 | - |  |  | SI | Vive con madre |
| Q35 | - |  |  | SI | Vive con padre |
| Q36 | - |  |  | SI | Vive en institución |
| Q37 | - |  |  | SI | Vive con otros |
| Q38 | - |  |  | SI | Observaciones |
| Q39 | - |  |  | SI | Nivel de instrucción madre o sustituta |
| Q40 | - |  |  | SI | Nivel de instrucción padre o sustituto |
| Q41 | - |  |  | SI | Nivel instrucción pareja |
| Q42 | - |  |  | SI | Ocupación madre o sustituta |
| Q43 | - |  |  | SI | Ocupación padre o sustituto |
| Q44 | - |  |  | SI | Ocupación pareja |
| Q45 | - |  |  | SI | Comparte cama |
| Q46 | - |  |  | SI | Con quién |
| Q47 | - |  |  | SI | Percepción del adolescente sobre su familia |
| Q48 | - |  |  | SI | Condiciones sanitarias |
| Q49 | - |  |  | SI | Hacinamiento |
| Q50 | - |  |  | SI | Observaciones (Vivienda) |
| Q51 | - |  |  | SI | Estudia |
| Q52 | - |  |  | SI | Nivel de Educación |
| Q53 | - |  |  | SI | Grado o curso |
| Q54 | - |  |  | SI | Años repetidos |
| Q55 | - |  |  | SI | Causa años Repetidos |
| Q56 | - |  |  | SI | Problemas en Institución Educativa |
| Q57 | - |  |  | SI | Violencia escolar |
| Q58 | - |  |  | SI | Deserción / exclusión |
| Q59 | - |  |  | SI | Causa deserción o exclusión escolar |
| Q60 | - |  |  | SI | Percepción de rendimiento respecto a la mayoría de... |
| Q61 | - |  |  | SI | Observaciones (Educación) |
| Q62 | - |  |  | SI | Trabaja |
| Q63 | - |  |  | SI | Horas x semana |
| Q64 | - |  |  | SI | Trabajo infantil |
| Q65 | - |  |  | SI | Trabajo juvenil |
| Q66 | - |  |  | SI | Peores formas |
| Q67 | - |  |  | SI | Servicio doméstico no remunerado peligroso |
| Q68 | - |  |  | SI | Razón de trabajo |
| Q69 | - |  |  | SI | Legalizado |
| Q70 | - |  |  | SI | Tipo de trabajo |
| Q71 | - |  |  | SI | Observaciones (Trabajo) |
| Q72 | - |  |  | SI | Aceptación |
| Q73 | - |  |  | SI | Pareja |
| Q74 | - |  |  | SI | Edad pareja (Años) |
| Q75 | - |  |  | SI | Edad pareja (Meses) |
| Q76 | - |  |  | SI | Violencia en la pareja |
| Q77 | - |  |  | SI | Amigos/as |
| Q78 | - |  |  | SI | Actividad física (horas por semana) |
| Q79 | - |  |  | SI | Tv (horas por día) |
| Q80 | - |  |  | SI | Computador / consola y otros (horas por día) |
| Q81 | - |  |  | SI | Otras actividades |
| Q82 | - |  |  | SI | Especificar otras actividades |
| Q83 | - |  |  | SI | Grooming |
| Q84 | - |  |  | SI | Cyberbullyng |
| Q85 | - |  |  | SI | Observaciones (Vida social) |
| Q86 | - |  |  | SI | Sueño normal |
| Q87 | - |  |  | SI | Horas por día |
| Q88 | - |  |  | SI | Alimentación adecuada |
| Q89 | - |  |  | SI | Comidas con familia |
| Q90 | - |  |  | SI | Alimentación especial |
| Q91 | - |  |  | SI | Especificar alimentación especial |
| Q92 | - |  |  | SI | Tabaco |
| Q93 | - |  |  | SI | Promedio cigarros / día |
| Q94 | - |  |  | SI | Alcoholismo |
| Q95 | - |  |  | SI | Marihuana |
| Q96 | - |  |  | SI | Otra sustancia |
| Q97 | - |  |  | SI | Especificar otra sustancia |
| Q98 | - |  |  | SI | Seguridad vial |
| Q99 | - |  |  | SI | Observaciones (Hábitos / consumo) |
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