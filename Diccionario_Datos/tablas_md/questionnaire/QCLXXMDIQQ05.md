# questionnaire.QCLXXMDIQQ05

> Mantención Dispositivos Invasivos : Catéteres Arteriales

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Mantención Dispositivos Invasivos : Catéteres Arteriales

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q05Q1 | varchar |  |  | SI | N° |
| Q05Q10 | varchar |  |  | SI | Comentarios |
| Q05Q2 | varchar |  |  | SI | Actividad |
| Q05Q3 | varchar |  |  | SI | Ubicación |
| Q05Q4 | varchar |  |  | SI | Tamaño Línea Arterial |
| Q05Q5 | varchar |  |  | SI | N° Días Línea Arterial |
| Q05Q6 | varchar |  |  | SI | Permeabilidad |
| Q05Q7 | varchar |  |  | SI | Sitio Inserción |
| Q05Q8 | varchar |  |  | SI | Estado Cobertura |
| Q05Q9 | varchar |  |  | SI | ¿Es necesario el DI? |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*