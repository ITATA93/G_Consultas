# questionnaire.QTCESOLAPATQQ51

> Solicitud de Examen Anatomía Patológica : Detalle de Contenedores

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Solicitud de Examen Anatomía Patológica : Detalle de Contenedores

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q51Q1 | varchar |  |  | SI | Órgano/Tejido |
| Q51Q10 | numeric |  |  | SI | N° de Muestras |
| Q51Q2 | varchar |  |  | SI | Localización |
| Q51Q3 | varchar |  |  | SI | Lateralidad |
| Q51Q4 | numeric |  |  | SI | N° de Contenedores |
| Q51Q5 | varchar |  |  | SI | Diagnóstico Clínico |
| Q51Q6 | varchar |  |  | SI | Lateralidad |
| Q51Q7 | varchar |  |  | SI | ID Contenedor |
| Q51Q8 | varchar |  |  | SI | Tipo de Contenedor |
| Q51Q9 | varchar |  |  | SI | Precisión / Detalle |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*