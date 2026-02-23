# questionnaire.QCLXXFHCLAP

> Ficha Salud Integral Adolescente (CLAP Modificada)

**Schema:** questionnaire
**Columnas:** 309
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ficha Salud Integral Adolescente (CLAP Modificada)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Control en Establecimiento |
| Q02 | varchar |  |  | SI | Establecimiento Educacional |
| Q03 | varchar |  |  | SI | Beneficiario Protección Social |
| Q04 | varchar |  |  | SI | País de Origen |
| Q05 | varchar |  |  | SI | Estado Civil |
| Q06 | varchar |  |  | SI | Pueblo Indígena |
| Q07 | varchar |  |  | SI | Acompañante |
| Q10 | varchar |  |  | SI | Descripción motivo de consulta |
| Q100 | numeric |  |  | SI | Edad Menarca / espermarca (años) |
| Q101 | numeric |  |  | SI | Edad Menarca / espermarca (meses) |
| Q102 | date |  |  | SI | Fecha de última menstruación |
| Q103 | varchar |  |  | SI | Fecha ultima menstruación desconocida |
| Q104 | varchar |  |  | SI | Ciclos regulares_old |
| Q105 | varchar |  |  | SI | Dismenorrea |
| Q106 | varchar |  |  | SI | Flujo patológico vaginal / secreción peneana |
| Q107 | varchar |  |  | SI | ITS / VIH |
| Q108 | varchar |  |  | SI | Especificar enfermedad de transmisión sexual |
| Q109 | varchar |  |  | SI | Tratamiento ITS/VIH |
| Q11 | varchar |  |  | SI | PERINATALES NORMALES |
| Q110 | varchar |  |  | SI | Tratamiento ITS/VIH de contactos |
| Q111 | numeric |  |  | SI | Embarazos |
| Q112 | numeric |  |  | SI | Hijos |
| Q113 | numeric |  |  | SI | Abortos |
| Q114 | varchar |  |  | SI | Observaciones (Gineco-Urológico) |
| Q115 | varchar |  |  | SI | Orientación sexual |
| Q116 | varchar |  |  | SI | Se identifica como: |
| Q117 | varchar |  |  | SI | Intención o conducta sexual |
| Q118 | numeric |  |  | SI | Edad de inicio intención o conducta sexual |
| Q119 | varchar |  |  | SI | Relaciones sexuales con |
| Q12 | varchar |  |  | SI | Alergias |
| Q120 | varchar |  |  | SI | Pareja sexual |
| Q121 | varchar |  |  | SI | Dificultades en relaciones sexuales |
| Q122 | varchar |  |  | SI | ¿Uso habitual del condón? |
| Q123 | varchar |  |  | SI | Doble protección  |
| Q124 | varchar |  |  | SI | Uso MAC actual |
| Q125 | varchar |  |  | SI | Especificar cual MAC? |
| Q126 | varchar |  |  | SI | Razón no uso MAC |
| Q127 | varchar |  |  | SI | Consejería uso MAC |
| Q128 | varchar |  |  | SI | ACO de emergencia |
| Q129 | varchar |  |  | SI | Violencia sexual |
| Q13 | varchar |  |  | SI | Vacunas completas |
| Q130 | varchar |  |  | SI | ¿Ha existido reparación? |
| Q131 | varchar |  |  | SI | Observaciones (Sexualidad) |
| Q132 | varchar |  |  | SI | Imagen corporal |
| Q133 | varchar |  |  | SI | Vida con proyecto |
| Q134 | varchar |  |  | SI | Bienestar emocional |
| Q135 | varchar |  |  | SI | Suicidio amigo/a o familiar cercano |
| Q136 | varchar |  |  | SI | Ideación suicida (último mes) |
| Q137 | varchar |  |  | SI | Intento suicida (últimos 3 meses) |
| Q138 | varchar |  |  | SI | Referente adulto |
| Q139 | varchar |  |  | SI | Nombre Referente |
| Q14 | varchar |  |  | SI | Enf. Importantes |
| Q140 | numeric |  |  | SI | Teléfono referente |
| Q141 | varchar |  |  | SI | Observaciones (Situación Psicoemocional) |
| Q142 | varchar |  |  | SI | Peso (Kg) |
| Q142ObsDR | varchar |  | FK | SI | Peso (Kg) DR |
| Q143 | varchar |  |  | SI | Talla (cm) |
| Q143ObsDR | varchar |  | FK | SI | Talla (cm) DR |
| Q144 | numeric |  |  | SI | Desviación estándar  (Talla) |
| Q145 | varchar |  |  | SI | Perímetro Cintura (cm) |
| Q145ObsDR | varchar |  | FK | SI | Perímetro Cintura (cm) DR |
| Q146 | varchar |  |  | SI | IMC |
| Q147 | numeric |  |  | SI | DE (IMC) |
| Q148 | varchar |  |  | SI | Presión arterial sistólica |
| Q148ObsDR | varchar |  | FK | SI | Presión arterial sistólica DR |
| Q149 | varchar |  |  | SI | Presión arterial diastólica |
| Q149ObsDR | varchar |  | FK | SI | Presión arterial diastólica DR |
| Q15 | varchar |  |  | SI | Discapacidad |
| Q150 | varchar |  |  | SI | Tanner mama |
| Q150ObsDR | varchar |  | FK | SI | Tanner mama DR |
| Q151 | varchar |  |  | SI | Tanner genital |
| Q151ObsDR | varchar |  | FK | SI | Tanner genital DR |
| Q152 | bit |  |  | SI | Con foto |
| Q153 | varchar |  |  | SI | Aspecto general |
| Q154 | varchar |  |  | SI | Agudeza visual |
| Q155 | varchar |  |  | SI | Agudeza auditiva |
| Q156 | varchar |  |  | SI | Salud bucal |
| Q157 | varchar |  |  | SI | Tiroides |
| Q158 | varchar |  |  | SI | Cardiopulmonar |
| Q159 | varchar |  |  | SI | Abdomen |
| Q16 | varchar |  |  | SI | Accidente relevante |
| Q160 | varchar |  |  | SI | Columna |
| Q161 | varchar |  |  | SI | Extremidades |
| Q162 | varchar |  |  | SI | Observaciones (Examen Físico) |
| Q163 | varchar |  |  | SI | Detección de Riesgo |
| Q164 | varchar |  |  | SI | Otro riesgo |
| Q165 | varchar |  |  | SI | Impresión Diagnóstica Integral (No diagnósticos) |
| Q166 | date |  |  | SI | Fecha Próxima Visita |
| Q167 | varchar |  |  | SI | Alertas Antecedentes Personales |
| Q168 | varchar |  |  | SI | Alertas Antecedentes Familiares |
| Q169 | varchar |  |  | SI | Alertas Educación |
| Q17 | varchar |  |  | SI | Cirugía / hospitalizaciones |
| Q170 | varchar |  |  | SI | Alertas Trabajo |
| Q171 | varchar |  |  | SI | Alertas Vida Social |
| Q172 | varchar |  |  | SI | Alertas Hábitos / Consumo |
| Q173 | varchar |  |  | SI | Alertas Gineco-Urológicas |
| Q174 | varchar |  |  | SI | Alertas Sexualidad |
| Q175 | varchar |  |  | SI | Alertas Situación Psicoemocional |
| Q176 | varchar |  |  | SI | Alertas Examen Físico |
| Q177 | varchar |  |  | SI | Alertas de Detección de Riesgos |
| Q178 | varchar |  |  | SI | Vive Con |
| Q179 | varchar |  |  | SI | Nivel de Instrucción de la Familia |
| Q18 | varchar |  |  | SI | Uso medicamentos |
| Q180 | varchar |  |  | SI | Detección Riesgo |
| Q181 | varchar |  |  | SI | Indicaciones e Interconsultas |
| Q182 | varchar |  |  | SI | Nombrar Institución |
| Q183 | varchar |  |  | SI | Modalidad de Estudio |
| Q184 | numeric |  |  | SI | Clases Virtuales (Horas al día) |
| Q185 | numeric |  |  | SI | Exposición a Pantallas (Horas al día) |
| Q186 | varchar |  |  | SI | Acceso a redes sociales |
| Q187 | varchar |  |  | SI | Violencia Virtual |
| Q188 | varchar |  |  | SI | Alimentación Inadecuada |
| Q189 | varchar |  |  | SI | ¿Ya tuvo la menarquia o espermarquia? |
| Q19 | varchar |  |  | SI | Problemas salud mental |
| Q190 | varchar |  |  | SI | Ritmo menstrual Duración (días menstruación):N/S-N... |
| Q191 | varchar |  |  | SI | Ritmo menstrual: Periodicidad (intervalos):N/S-N/C |
| Q192 | varchar |  |  | SI | ¿Ha tenido relaciones sexuales? |
| Q193 | varchar |  |  | SI | ¿Pareja sexual? |
| Q194 | numeric |  |  | SI | ¿Edad pareja? |
| Q195 | numeric |  |  | SI | ¿Edad inicio relaciones sexuales? |
| Q196 | varchar |  |  | SI | ¿Tipo practica sexual? |
| Q197 | varchar |  |  | SI | ¿Ha tenido episodios de violencia física, en su re... |
| Q198 | varchar |  |  | SI | ¿Ha tenido episodios de violencia sexual, en su re... |
| Q199 | varchar |  |  | SI | ¿Ha tenido episodios de violencia psicológica, en ... |
| Q20 | varchar |  |  | SI | Violencia |
| Q200 | varchar |  |  | SI | ¿Antecedente de IVE? |
| Q201 | varchar |  |  | SI | ¿Estado de ánimo en el último mes? |
| Q202 | varchar |  |  | SI | ¿Deseo de estar muerto en el último mes? |
| Q203 | varchar |  |  | SI | Correo electrónico |
| Q204 | numeric |  |  | SI | Desviación estándar (Peso) |
| Q205 | numeric |  |  | SI | Desviación estándar (Perímetro Cintura) |
| Q206 | varchar |  |  | SI | Presión Arterial |
| Q207 | varchar |  |  | SI | Nacionalidades |
| Q208 | varchar |  |  | SI | Detalle Nacionalidad |
| Q209 | varchar |  |  | SI | Consulta Principal N° |
| Q21 | varchar |  |  | SI | Judiciales |
| Q210 | date |  |  | SI | Fecha consulta principal |
| Q211 | varchar |  |  | SI | ¿Cuales Problemas? |
| Q212 | varchar |  |  | SI | ¿Cuales actividades físicas? |
| Q213 | varchar |  |  | SI | Plataformas virtuales |
| Q214 | varchar |  |  | SI | Ritmo menstrual |
| Q215 | varchar |  |  | SI | Periodicidad |
| Q216 | varchar |  |  | SI | Tranquilo |
| Q217 | varchar |  |  | SI | Desanimado |
| Q218 | varchar |  |  | SI | Nervioso/estresado |
| Q219 | varchar |  |  | SI | Irritable |
| Q22 | varchar |  |  | SI | Otros |
| Q220 | varchar |  |  | SI | Estado de Ánimo |
| Q221 | varchar |  |  | SI | Referente Adulto (Otro) |
| Q222 | varchar |  |  | SI | Piel |
| Q223 | varchar |  |  | SI | Orientación Sexual |
| Q224 | varchar |  |  | SI | Vía vaginal |
| Q225 | varchar |  |  | SI | Vía oral |
| Q226 | varchar |  |  | SI | Vía anal |
| Q227 | varchar |  |  | SI | Prácticas Sexuales |
| Q228 | varchar |  |  | SI | Fecha Última Menstruación |
| Q229 | varchar |  |  | SI | Acompañante (Otro) |
| Q23 | varchar |  |  | SI | Observaciones (Antecedentes Personales) |
| Q230 | varchar |  |  | SI | Riesgo de Trastorno por Consumo de Alcohol y Otras... |
| Q231 | varchar |  |  | SI | A. ¿En los últimos 12 meses has consumido? |
| Q232 | varchar |  |  | SI | Alcohol |
| Q233 | varchar |  |  | SI | Marihuana |
| Q234 | varchar |  |  | SI | Otra sustancia |
| Q235 | varchar |  |  | SI | B1. ¿Alguna vez has andado en AUTO manejado por al... |
| Q236 | varchar |  |  | SI | B2. ¿Has usado alguna vez alcohol o drogas para RE... |
| Q237 | varchar |  |  | SI | B3. ¿Has consumido alguna vez alcohol o drogas est... |
| Q238 | varchar |  |  | SI | B4. ¿Has OLVIDADO alguna vez cosas que hiciste mie... |
| Q239 | varchar |  |  | SI | B5. ¿Te ha dicho tu familia o amigos que debes dis... |
| Q24 | varchar |  |  | SI | Enf. Importantes (Familiares) |
| Q240 | varchar |  |  | SI | B6. ¿Te has metido alguna vez en PROBLEMAS mientra... |
| Q241 | varchar |  |  | SI | Puntaje total B |
| Q242 | varchar |  |  | SI | Sexo |
| Q243 | varchar |  |  | SI | Género |
| Q244 | varchar |  |  | SI | 1.TRABAJO |
| Q245 | varchar |  |  | SI | 10.VIOENCIA DE PAREJA |
| Q246 | varchar |  |  | SI | 4.RIESGO SUICIDA |
| Q247 | varchar |  |  | SI | 5.REFERENTE ADULTO/A |
| Q248 | varchar |  |  | SI | 6.TANNER |
| Q249 | varchar |  |  | SI | 3.RITMO MENSTRUAL |
| Q25 | varchar |  |  | SI | Obesidad |
| Q250 | varchar |  |  | SI | horas por día |
| Q251 | varchar |  |  | SI | 5.ACCESO A: |
| Q252 | varchar |  |  | SI | Solo / a |
| Q253 | varchar |  |  | SI | madre |
| Q254 | varchar |  |  | SI | padre |
| Q255 | varchar |  |  | SI | en institución |
| Q256 | varchar |  |  | SI | con otros |
| Q257 | varchar |  |  | SI | Diagrama Familiar |
| Q258 | varchar |  |  | SI | Centro de Salud |
| Q259 | varchar |  |  | SI | Código |
| Q26 | varchar |  |  | SI | Problemas salud mental (Familiar) |
| Q260 | varchar |  |  | SI | H.C.N° |
| Q261 | varchar |  |  | SI | Nombre responsable/profesion |
| Q262 | varchar |  |  | SI | Especificar alimentación especial |
| Q263 | varchar |  |  | SI | Ciclos regulares |
| Q27 | varchar |  |  | SI | Violencia intrafamiliar |
| Q28 | varchar |  |  | SI | Alcohol y otras drogas |
| Q29 | varchar |  |  | SI | Madre y/o padre adolescente |
| Q30 | varchar |  |  | SI | Judiciales (Familiares) |
| Q31 | varchar |  |  | SI | Otros (Familiares) |
| Q32 | varchar |  |  | SI | Observaciones (Antecedentes Familiares) |
| Q33 | varchar |  |  | SI | Vive Solo/a |
| Q34 | varchar |  |  | SI | Vive con madre |
| Q35 | varchar |  |  | SI | Vive con padre |
| Q36 | varchar |  |  | SI | Vive en institución |
| Q37 | varchar |  |  | SI | Vive con otros |
| Q38 | varchar |  |  | SI | Observaciones |
| Q39 | varchar |  |  | SI | Nivel de instrucción madre o sustituta |
| Q40 | varchar |  |  | SI | Nivel de instrucción padre o sustituto |
| Q41 | varchar |  |  | SI | Nivel instrucción pareja |
| Q42 | varchar |  |  | SI | Ocupación madre o sustituta |
| Q43 | varchar |  |  | SI | Ocupación padre o sustituto |
| Q44 | varchar |  |  | SI | Ocupación pareja |
| Q45 | varchar |  |  | SI | Comparte cama |
| Q46 | varchar |  |  | SI | Con quién |
| Q47 | varchar |  |  | SI | Percepción del adolescente sobre su familia |
| Q48 | varchar |  |  | SI | Condiciones sanitarias |
| Q49 | varchar |  |  | SI | Hacinamiento |
| Q50 | varchar |  |  | SI | Observaciones (Vivienda) |
| Q51 | varchar |  |  | SI | Estudia |
| Q52 | varchar |  |  | SI | Nivel de Educación |
| Q53 | numeric |  |  | SI | Grado o curso |
| Q54 | numeric |  |  | SI | Años repetidos |
| Q55 | varchar |  |  | SI | Causa años Repetidos |
| Q56 | varchar |  |  | SI | Problemas en Institución Educativa |
| Q57 | varchar |  |  | SI | Violencia escolar |
| Q58 | varchar |  |  | SI | Deserción / exclusión |
| Q59 | varchar |  |  | SI | Causa deserción o exclusión escolar |
| Q60 | varchar |  |  | SI | Percepción de rendimiento respecto a la mayoría de... |
| Q61 | varchar |  |  | SI | Observaciones (Educación) |
| Q62 | varchar |  |  | SI | Trabaja |
| Q63 | numeric |  |  | SI | Horas x semana |
| Q64 | varchar |  |  | SI | Trabajo infantil |
| Q65 | varchar |  |  | SI | Trabajo juvenil |
| Q66 | varchar |  |  | SI | Peores formas |
| Q67 | varchar |  |  | SI | Servicio doméstico no remunerado peligroso |
| Q68 | varchar |  |  | SI | Razón de trabajo |
| Q69 | varchar |  |  | SI | Legalizado |
| Q70 | varchar |  |  | SI | Tipo de trabajo |
| Q71 | varchar |  |  | SI | Observaciones (Trabajo) |
| Q72 | varchar |  |  | SI | Aceptación |
| Q73 | varchar |  |  | SI | Pareja |
| Q74 | numeric |  |  | SI | Edad pareja (Años) |
| Q75 | numeric |  |  | SI | Edad pareja (Meses) |
| Q76 | varchar |  |  | SI | Violencia en la pareja |
| Q77 | varchar |  |  | SI | Amigos/as |
| Q78 | numeric |  |  | SI | Actividad física (horas por semana) |
| Q79 | numeric |  |  | SI | Tv (horas por día) |
| Q80 | numeric |  |  | SI | Computador / consola y otros (horas por día) |
| Q81 | varchar |  |  | SI | Otras actividades |
| Q82 | varchar |  |  | SI | Especificar otras actividades |
| Q83 | varchar |  |  | SI | Grooming |
| Q84 | varchar |  |  | SI | Cyberbullyng |
| Q85 | varchar |  |  | SI | Observaciones (Vida social) |
| Q86 | varchar |  |  | SI | Sueño normal |
| Q87 | numeric |  |  | SI | Horas por día |
| Q88 | varchar |  |  | SI | Alimentación adecuada |
| Q89 | numeric |  |  | SI | Comidas con familia |
| Q90 | varchar |  |  | SI | Alimentación especial |
| Q91 | varchar |  |  | SI | Especificar alimentación especial(old) |
| Q92 | varchar |  |  | SI | Tabaco |
| Q93 | numeric |  |  | SI | Promedio cigarros / día |
| Q94 | varchar |  |  | SI | Alcoholismo |
| Q95 | varchar |  |  | SI | Marihuana |
| Q96 | varchar |  |  | SI | Otra sustancia |
| Q97 | varchar |  |  | SI | Especificar otra sustancia |
| Q98 | varchar |  |  | SI | Seguridad vial |
| Q99 | varchar |  |  | SI | Observaciones (Hábitos / consumo) |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*