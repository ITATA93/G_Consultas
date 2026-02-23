# questionnaire.QCLXXEXNEUQQ100

> Examen Neurológico y Físico : Fuerza y resistencia

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Neurológico y Físico : Fuerza y resistencia

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q100Q1 | varchar |  |  | SI | Segmento / músculo |
| Q100Q2 | varchar |  |  | SI | Lateralidad |
| Q100Q3 | varchar |  |  | SI | Fuerza |
| Q100Q4 | varchar |  |  | SI | Tono |
| Q100Q5 | varchar |  |  | SI | Trofismo |
| Q100Q6 | varchar |  |  | SI | Comentarios |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*