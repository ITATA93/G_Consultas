# questionnaire.QTCESOLAPATQQ54

> Solicitud de Examen Anatomía Patológica : Antecedentes Último Examen

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Solicitud de Examen Anatomía Patológica : Antecedentes Último Examen

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q54Q1 | varchar |  |  | SI | Tipo Examen |
| Q54Q2 | date |  |  | SI | Fecha |
| Q54Q3 | varchar |  |  | SI | Resultado |
| Q54Q4 | varchar |  |  | SI | Laboratorio |
| Q54Q5 | varchar |  |  | SI | Región |
| Q54Q6 | varchar |  |  | SI | País |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*